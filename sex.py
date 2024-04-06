import league_connection
from league_connection import LeagueConnection
from league_client.summoner import get_summoner_puuid
from league_client.match_history import get_match_history
import time
import traceback
from datetime import date, datetime, timedelta
import win32gui, psutil, json, os
from winotify import Notification
import util_function
from win10toast import ToastNotifier
#riot_lockfile = 'C:/Users/Za/AppData/Local/Riot Games/Riot Client/Config/lockfile'
#riot_connection = LeagueConnection(riot_lockfile)
LEAGUE_LOCK_FILE = 'C:/Program Files (x86)/Riot Games/League of Legends/ayyy'
CONFIG_FILE_LOCATION = "params.ini"
ConfigData = util_function.load_config_preprocessed (CONFIG_FILE_LOCATION)
#HISTORY_FILE_LOCATION = "PlayerHistory.ngga"
HISTORY_FILE_LOCATION = ConfigData["CoreSetting"]["savefilepath"]
#Hard coded value that is not meant to be changed
Keep = ['endOfGameResult', 'gameCreationDate', 'gameDuration',
        'gameMode', 'gameType']
GameName = 'League of Legends (TM) Client'
ClientName = 'League of Legends'
ClientExeName = 'LeagueClient.exe'
#GameModeList = ['CLASSIC', 'PRACTICETOOL', 'ARAM']
#GameTypeList = ['CUSTOM_GAME', 'MATCHED_GAME']
#GameModeList = ['CLASSIC', 'ARAM']
#GameTypeList = ['MATCHED_GAME']
GameModeList, GameTypeList = util_function.load_gamemode_gametype (ConfigData)
LolTaskRemoveList = ['LeagueCrashHandler64.exe','LeagueClientUxRender.exe',
                     'LeagueClientUx.exe','LeagueClient.exe']

def find_path(name):
    for pid in psutil.pids():
        if psutil.Process(pid).name() == name:
            #print ("FOUND ", name)
            return psutil.Process(pid).exe()
    #print ("find_path NOT FOUND!!!!!!", name)
def get_lockfile_path ():
    leagueClientLocation = find_path(ClientExeName)
    if os.path.exists(leagueClientLocation):
        parent_dir = os.path.split(leagueClientLocation)[0]
        LEAGUE_LOCK_FILE = os.path.join (parent_dir, 'lockfile').replace(os.sep, '/')
    return LEAGUE_LOCK_FILE
def get_running_process ():
    window_titles = set()
    def winEnumHandler( hwnd, ctx ):
        if win32gui.IsWindowVisible( hwnd ):
            window_titles.add(win32gui.GetWindowText( hwnd ) )
    win32gui.EnumWindows(winEnumHandler, None)
    return window_titles
def shutdown_lol ():
    while (True):
        flag = 0
        for proc in psutil.process_iter():
            try:
                if proc.name() in LolTaskRemoveList:
                    proc.kill()
                    flag = 1
                    break
            except:
                pass
        if (flag == 0):
            time.sleep (3)
            return
def read_history(save_name = HISTORY_FILE_LOCATION):
    GameHistoryList = []
    try:
        with open(save_name, "r", encoding = "UTF-16") as fp:
            GameHistoryList = json.load(fp)
    except Exception as e:
        print ("File read exception: ", e)
    return GameHistoryList
def write_history (GameHistoryList, save_name = HISTORY_FILE_LOCATION):
    with open(save_name, "w", encoding = "UTF-16") as fp:
        json.dump(GameHistoryList, fp)
def hours_diff_check (date1, date2, Hours):
    return abs(date1 - date2) < timedelta(hours=Hours)
def printReason (KillReason = "nigger"):
    toast = ToastNotifier()
    toast = Notification(app_id="LoL Rehab",
             title="League is killed, fuck you",
             msg=KillReason)
    toast.show()
    toast = ToastNotifier()
    toast = Notification(app_id="LoL Rehab",
             title="Touch some grass",
             msg="You have set a goal for this, obey it!\n.Get something else to do man, if you have nothing to do, it's your fault, stop playing the game")
    toast.show()
def check_eligibility (GameHistoryList, ConfigData, GameModeList, GameTypeList, verbose = 0):
#Check if the player is eligible to play, return True if allowed
    SumGame = 0
    SumTime = 0
    def get_plays_data (GameHistoryList, maxHourDifference, GameModeList, GameTypeList, verbose = 0):
        Now = datetime.now()
        SumGame = 0
        SumTime = 0
        for i in range (0, len (GameHistoryList)):
            #Could be done faster with binary search, but list is only 20-50 items so fuck it
            #Convert game creation date to datetime object
            TimeStr = datetime.strptime(GameHistoryList[i]['gameCreationDate'], "%Y-%m-%dT%H:%M:%S.%fZ")
            GameMode = GameHistoryList[i]['gameMode']
            GameType = GameHistoryList[i]['gameType']
            if (GameMode in GameModeList) and (GameType in GameTypeList) and hours_diff_check(TimeStr, Now, maxHourDifference):
                SumGame+=1
                SumTime+=GameHistoryList[i]['gameDuration']
        SumTime = SumTime/60
        if (verbose == 1):
            print ('Game count: ',SumGame,', Total time: ',SumTime)
        return SumGame, SumTime
    def check_plays (GameHistoryList, Limit, TimeOffset, GameModeList, GameTypeList, verbose = 0):
            
        Now = datetime.now()
        if ((Now - timedelta(hours=TimeOffset)).weekday() not in Limit[4]) or (
            Now.hour>=Limit[5][1]) or (Now.hour<Limit[5][0]):
            return True
        SumGame, SumTime = get_plays_data (GameHistoryList, Limit[3], GameModeList, GameTypeList, verbose = verbose)
        if SumTime > Limit [2]:
            #print ('Game count: ',SumGame,', Total time: ',SumTime,' minutes)
            niggerString = "Total time exceeded, you have played for "+ str(int(SumTime+0.5))+ " minutes, maximum time allowed is "+ str(Limit[2]) +" minutes. Ruleset name: \'"+ str(Limit[6])+"\'"
            printReason (niggerString)            
            return False
        if (SumTime > Limit [1]) and (SumGame > Limit [0]):
            niggerString = "Total game count and game time exceeded, you have played "+ str(SumGame)+" games for "+ str(int(SumTime+0.5))+" minutes, maximum game count allowed is "+ str(Limit[0])+" games.Ruleset name: \'",Limit[6],"\'"
            printReason (niggerString)
            return False
        return True
    tempFlag = True
    for limit in ConfigData["limits"]:
        if (check_plays (GameHistoryList, limit, ConfigData["CoreSetting"]['timeoffset'], GameModeList, GameTypeList, verbose = verbose) == False):
            #return False, limit[-1]
            tempFlag = False
            print ("Not allowed, reason: ",limit)
        else:
            if (verbose == 1):
                print ("Allowed, reason: ",limit)
    return tempFlag

GameHistoryList = read_history()
SaveFag = 0
CheckingTime = 10
SumGame = 0
print ("Initializing")
while (True):
    RunningProcess = get_running_process()
    if GameName in RunningProcess:
        CheckingTime = 5
        print ("Game is running, skipping")
        time.sleep (10)
    if ClientName in RunningProcess:
        try:
            if check_eligibility (GameHistoryList, ConfigData, GameModeList, GameTypeList, 0) == False:
                shutdown_lol ()
                time.sleep (3)
                continue
            time.sleep (3) #3 seconds sleep cuz League is slow AF
            #Setup
            LEAGUE_LOCK_FILE = get_lockfile_path()
            Connection = LeagueConnection(LEAGUE_LOCK_FILE)
            A = get_match_history(Connection, get_summoner_puuid(Connection))
            #Current time
            #Loop over all 20 games in current player's history
            TempTime = 0
            TempGame = 0
            for i in range (19, -1, -1):
                Niggus = {}
                for tag in Keep:
                    Niggus[tag] = A['games']['games'][i][tag]
                #If current game is not in list, add it to the list
                #and update the tag to update the history file later.
                if Niggus not in GameHistoryList:
                    GameHistoryList.append (Niggus)
                    SaveFag = 1
                #Check if current game is counted depending on game mode
                TempGame += 1
                TempTime += A['games']['games'][i]['gameDuration']
            #There is a new game recorded, so we start updating the file.
            if (SaveFag == 1):
                print ('\n_______________________________')
                print ("Adding game time (hour): ",TempTime/60/60)
                print ("Adding games count: ",TempGame)
                write_history (GameHistoryList)
                SaveFag = 0
            elif (SaveFag == 0):
                SaveFag = -1
                CheckingTime = min(int(CheckingTime * 2), 600)
                print ("Nothing new, skipping")
            if check_eligibility (GameHistoryList, ConfigData, GameModeList, GameTypeList, verbose = 0) == False:
                shutdown_lol ()
                CheckingTime = 10
            else:
                CheckingTime = 60
            time.sleep (CheckingTime) #100 seconds sleep
        except Exception as ex:
            print ("Exception! Game closed or problem with lockfile")
            print ("Exception details: ",ex)
            print(traceback.format_exc())
            #raise #raise the exception instead of ommiting it.
    else:
        pass
    time.sleep (3) #1 seconds sleep


