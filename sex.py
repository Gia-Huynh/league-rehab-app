import league_connection
from league_connection import LeagueConnection
from league_client.summoner import get_summoner_puuid
from league_client.match_history import get_match_history
import time
from datetime import date, datetime
#from dateutil import parser
import win32gui, psutil, json, os

#riot_lockfile = 'C:/Users/Za/AppData/Local/Riot Games/Riot Client/Config/lockfile'
#riot_connection = LeagueConnection(riot_lockfile)
league_lockfile = 'C:/Program Files (x86)/Riot Games/League of Legends/ayyy'
default_save_file = "PlayerHistory.ngga"
def save_config (config_data, filename):
    pass
def load_config (filename):
    return config_data
#Hard coded value that is not meant to be changed
Keep = ['endOfGameResult', 'gameCreationDate', 'gameDuration',
        'gameMode', 'gameType']
GameName = 'League of Legends (TM) Client'
ClientName = 'League of Legends'
ClientExeName = 'LeagueClient.exe'
#GameModeList = ['CLASSIC', 'PRACTICETOOL', 'ARAM']
GameModeList = ['CLASSIC', 'PRACTICETOOL']
GameTypeList = ['CUSTOM_GAME', 'MATCHED_GAME']
LolTaskRemoveList = ['LeagueCrashHandler64.exe','LeagueClientUxRender.exe',
                     'LeagueClientUx.exe','LeagueClient.exe']

def findPath(name):
    for pid in psutil.pids():
        if psutil.Process(pid).name() == name:
            print ("FOUND")
            return psutil.Process(pid).exe()
        #elif len(psutil.Process(pid).name()) > 15:
        #    print (psutil.Process(pid).name())
    print ("findPath NOT FOUND!!!!!!")
def getLockfilePath ():
    leagueClientLocation = findPath(client_exe_name)
    if os.path.exists(leagueClientLocation):
        parent_dir = os.path.split(leagueClientLocation)[0]
        league_lockfile = os.path.join (parent_dir, 'lockfile').replace(os.sep, '/')
    return league_lockfile
def get_running_process ():
    window_titles = set()
    def winEnumHandler( hwnd, ctx ):
        if win32gui.IsWindowVisible( hwnd ):
            window_titles.add(win32gui.GetWindowText( hwnd ) )
    win32gui.EnumWindows(winEnumHandler, None)
    return window_titles
def shutdown_lol ():
    for proc in psutil.process_iter():
        try:
            if proc.name() in LolTaskRemoveList:
                proc.kill()
        except:
            pass
def diff_dates (date1, date2):
    return abs(date2-date1).days
def readHistory(save_name = default_save_file):
    current_list = []
    try:
        with open(save_name, "r", encoding = "UTF-16") as fp:
            current_list = json.load(fp)
    except Exception as e:
        print ("File read exception: ", e)
    return current_list
def writeHistory (current_list, save_name = default_save_file):
    with open(save_name, "w", encoding = "UTF-16") as fp:
        json.dump(current_list, fp)
current_list = readHistory()
save_fag = 0
checking_time = 10
while (True):
    running_process = get_running_process()
    if game_name in running_process:
        checking_time = 5
        print ("Game is running, skipping")
        time.sleep (15)
    if client_name in running_process:
        try:
            time.sleep (5) #5 seconds sleep cuz League is slow AF
            #Setup
            league_lockfile = getLockfilePath()
            total_time = 0
            total_game = 0
            connection = LeagueConnection(league_lockfile)
            A = get_match_history(connection, get_summoner_puuid(connection))
            #Current time
            now = datetime.now()
            #Loop over all 20 games in current player's history
            for i in range (19, -1, -1):
                niggus = {}
                for tag in keep:
                    niggus[tag] = A['games']['games'][i][tag]
                #If current game is not in list, add it to the list
                #and update the tag to update the history file later.
                if niggus not in current_list:
                    current_list.append (niggus)
                    save_fag = 1
                #Check if current game is counted depending on game mode
                if (A['games']['games'][i]['gameMode'] in GameModeList):
                    total_game += 1
                    total_time += A['games']['games'][i]['gameDuration']
                #Get game start date string
                test_time = A['games']['games'][i]['gameCreationDate']
                #Convert duration string to datetime object
                test_time_str = datetime.strptime(test_time, "%Y-%m-%dT%H:%M:%S.%fZ")
                #print (diff_dates(test_time_str, now), end = ' ')
            #There is a new game recorded, so we start updating the file.
            if (save_fag == 1):
                print ('\n_______________________________')
                print ("Total game time (hour): ",total_time/60/60)
                print ("Total games count: ",total_game)
                writeHistory (current_list)
                save_fag = 0
            elif (save_fag == 0):
                save_fag = -1
                checking_time = min(int(checking_time * 2), 600)
                print ("Nothing new, skipping")
            time.sleep (checking_time) #100 seconds sleep
        except Exception as ex:
            print ("Exception! Game closed or problem with lockfile")
            print ("Exception details: ",ex)
            #raise #raise the exception instead of ommiting it.
    else:
        print ("League not running")
    time.sleep (10) #10 seconds sleep


