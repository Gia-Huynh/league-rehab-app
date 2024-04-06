import util_function
import json
#CONFIG_FILE_LOCATION = 
ConfigData = util_function.load_config ("paramsBak.ini")
print ("_____________________________\n IF YOU DON'T KNOW ANYTHING, just press enter without typing any value, the code will set the default value for you\n")

ConfigData["CoreSetting"]["TimeOffset"] = str(int(input ("Offset time (default value: 6) \nExample: Entered 6 means that any game played before 6am of a day will be counted as the day before, useful\
 if you don't want to reset the gaming counter after midnight\nEnter offset time: ") or 6))

ConfigData["GameTypeList"]["CUSTOM_GAME"] = str(int(input ("Do you want to count custom games? (Enter number 1 for yes or 0 for no)\n (Default: 0): ") or 0))
ConfigData["GameTypeList"]["MATCHED_GAME"] = str(int(input ("Do you want to count normal match-making games? (Enter number 1 for yes or 0 for no)\n (Default: 1): ") or 1))

ConfigData["GameModeList"]["CLASSIC"] = str(int(input ("Do you want to count classic Summoner's Rift games? (Enter number 1 for yes or 0 for no)\n (Default: 1): ") or 1))
ConfigData["GameModeList"]["ARAM"] = str(int(input ("Do you want to count Aram games? (Enter 1 or 0)\n (Default: 1): ") or 1))
ConfigData["GameModeList"]["PRACTICETOOL"] = str(int(input ("Do you want to count Practice Tool games? (Enter 1 or 0)\n (Default: 0): ") or 0))

vibin = int(input ("Do you want to start configurate game time limit? (Enter 1 for yes, 0 for no)\n (Default: 0): ") or 0)
def getOneLimit ():
    timeFrame = int(input ("Enter time frame for the limit (in hours), game played before this time will not be counted\n(game played 2 days ago will not be counted if timeframe is 24hours)\n\
[For reference, 1 day = 24 hours, 3 days = 72 hours, 1 week = 168 hours, 1 month = 672 hours]\nEnter time frame (in hours): "))
    DayInWeekApply = [int (x) for x in input ("Enter day in week that this limit apply (0 for Monday, 6 for Sunday) (Example: 0,1,2,3,4 = Weekday; 5,6 = Weekend)\n\
Enter multiple value, seperated by comma: ").split (',')]
    TimeInDayApply = [int (x) for x in (input ("Enter time in day that this value is applicable. (Default: 0, 24; which mean apply in whole day)\n\
(Enter two number, seperated by comma): ").split (',') or [0, 24])]
    print ("\n\n__________________\nGame count limit, min time limit, max time limit, explained:\n\
If you have reached your game count limit but total time played does not meet min time limit\n\
(example: 2 games that enemy team surrendered early), you will still be allowed to play until you meet the min time limit\n\
On the contrast, if you meet the max time limit, you are not allowed anymore (example: 1 game that takes 70 minutes).\n")
    GameCount = int(input ("Game count limit\n(Example: 2 games a day, or -1 for no game, or 999 for no limit).\n Enter value: "))
    MinTime = int(input ("Minimum allowed game time,\nCalculated good default value: " + str(17+(GameCount-1)*22) + ".\n Enter value: "))
    MaxTime = int(input ("Maximum allowed game time,\nCalculated good default value: " + str(GameCount*29) + ".\n Enter value: "))
    Name = input ("Enter name for this limit: ")
    js = '%s' % json.dumps([GameCount, MinTime, MaxTime, timeFrame, DayInWeekApply, TimeInDayApply,Name])
    return js

if vibin == 1:
    print ("_____________________________\nGame counts + Game time limit configurating\n")
    print ("Here, you can make many different limits that may be apply at different day in week (weekday limit, weekend limit) or different length (daily 24 hours limit, monthly 672 hours limit)")
    niggerList = []
    limitCount = 0
    while (True):
        print ("________________________\nLimit ",limitCount,": ")
        limitCount += 1
        niggerList.append(getOneLimit())
        response = input ("Continue adding another limit? (y/n): ")
        if response == "y":
            pass
        else:
            break
    finalString = niggerList[0]
    for i in range (1, len (niggerList)):
        finalString = finalString + ', \n' + niggerList[i]
    ConfigData["limits"]["limits"] = '['+finalString+']'
util_function.save_config (ConfigData, "params.ini")
print ("Config saved! Program exitting.")
