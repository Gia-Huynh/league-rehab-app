import win32gui, psutil, json, os, time
import sys
GameName = 'League of Legends (TM) Client'
ClientName = 'League of Legends'
ClientExeName = 'LeagueClient.exe'
#GameModeList = ['CLASSIC', 'PRACTICETOOL', 'ARAM']
#GameTypeList = ['CUSTOM_GAME', 'MATCHED_GAME']
LolTaskRemoveList = ['LeagueCrashHandler64.exe','LeagueClientUxRender.exe',
                     'LeagueClientUx.exe','LeagueClient.exe']

#print ("LeagueClient.exe" in (p.name() for p in psutil.process_iter()))
def print_all_process ():
    print ("_________")
    for proc in psutil.process_iter():
        try:
            if (proc.name()[0] == "L") or (proc.name()[0] == "l"):
                print (proc.name())
        except:
            pass
while True:
    print_all_process()
    time.sleep (5)
