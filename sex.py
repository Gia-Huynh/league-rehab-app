import league_connection
from league_connection import LeagueConnection
from league_client.summoner import get_summoner_puuid
from league_client.match_history import get_match_history
import time
from datetime import date, datetime
#from dateutil import parser
import win32gui, psutil, json

game_name = 'League of Legends (TM) Client'
client_name = 'League of Legends'
riot_lockfile = 'C:/Users/Za/AppData/Local/Riot Games/Riot Client/Config/lockfile'
league_lockfile = 'C:/Program Files (x86)/Riot Games/League of Legends/lockfile'
keep = ['endOfGameResult', 'gameCreationDate', 'gameDuration',
        'gameMode', 'gameType']
#GameModeList = ['CLASSIC', 'PRACTICETOOL', 'ARAM']
GameModeList = ['CLASSIC', 'PRACTICETOOL']
GameTypeList = ['CUSTOM_GAME', 'MATCHED_GAME']
LolTaskRemoveList = ['LeagueCrashHandler64.exe','LeagueClientUxRender.exe',
                     'LeagueClientUx.exe','LeagueClient.exe']
#GameModeList = ['CLASSIC']


def diff_dates (date1, date2):
    return abs(date2-date1).days
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
current_list = []
while (True):
    running_process = get_running_process()
    if client_name in running_process:
        try:
            total_time = 0
            total_game = 0
            save_fag = 0
            connection = LeagueConnection(league_lockfile)
            riot_connection = LeagueConnection(riot_lockfile)
            A = get_match_history(connection, get_summoner_puuid(connection))
            now = datetime.now()
            for tag in keep:
                print ('_______________________________')
                print (tag,': ', A['games']['games'][0][tag])
            for i in range (19, -1, -1):
                niggus = {}
                for tag in keep:
                    niggus[tag] = A['games']['games'][i][tag]
                if niggus not in current_list:
                    current_list.append (niggus)
                    save_fag = 1
                    print ("niggus ",niggus)
                else:
                    print ("Already in")
                if (A['games']['games'][i]['gameMode'] in GameModeList):
                    total_game += 1
                    total_time += A['games']['games'][i]['gameDuration']
                test_time = A['games']['games'][i]['gameCreationDate']
                test_time_str = datetime.strptime(test_time, "%Y-%m-%dT%H:%M:%S.%fZ")
                print (diff_dates(test_time_str, now), end = ' ')
            print ('\n_______________________________')
            print ("Total game time (hour): ",total_time/60/60)
            print ("Total games count: ",total_game)
            if (save_fag == 1):
                with open("test", "w") as fp:
                    json.dump(current_list, fp)
            time.sleep (5) #100 seconds sleep
        except Exception as ex:
            print ("Exception! Game closed or problem with lockfile")
            print ("Exception details: ",ex)
            #raise
    else:
        print ("League not running")
    time.sleep (10) #10 seconds sleep


