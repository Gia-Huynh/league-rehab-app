import win32gui, psutil, json, os
import sys
GameName = 'League of Legends (TM) Client'
ClientName = 'League of Legends'
ClientExeName = 'LeagueClient.exe'
#GameModeList = ['CLASSIC', 'PRACTICETOOL', 'ARAM']
#GameTypeList = ['CUSTOM_GAME', 'MATCHED_GAME']
LolTaskRemoveList = ['LeagueCrashHandler64.exe','LeagueClientUxRender.exe',
                     'LeagueClientUx.exe','LeagueClient.exe']

print ("LeagueClient.exe" in (p.name() for p in psutil.process_iter()))
for proc in psutil.process_iter():
    try:
        if (proc.name()[0] == "L") or (proc.name()[0] == "l"):
            print (proc.name())
    except:
        pass
