import configparser
import ast
def save_config (ConfigData, filename):
    with open(filename, 'w') as configfile:
        config.write(configfile)
def load_config (filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return config
def load_config_preprocessed (filename):
    settings = dict (load_config (filename))
    del settings["Help"]
    del settings['DEFAULT']
    for key, value in settings.items():
            settings[key] = dict (value)
    settings["limits"] = ast.literal_eval(settings["limits"]['limits'])
    settings["Quote"]['quotelist'] = ast.literal_eval(settings["Quote"]['quotelist'])
    for key, value in settings["CoreSetting"].items():
        try:
            settings["CoreSetting"][key] = int(value)
        except Exception as e:
            pass
    return settings
def load_gamemode_gametype (ConfigData):
    GameModeOGList = ["CLASSIC", "ARAM", "PRACTICETOOL"]
    GameTypeOGList = ["MATCHED_GAME", "CUSTOM_GAME"]
    GameModeList = []
    GameTypeList = []
    for a in GameModeOGList:
        if (ConfigData ["GameModeList"][a.lower()] == "1"):
            GameModeList.append (a)
    for a in GameTypeOGList:
        if (ConfigData ["GameTypeList"][a.lower()] == "1"):
            GameTypeList.append (a)
    return GameModeList, GameTypeList
    #if (ConfigData):
#a = load_config_preprocessed ('params.ini')
#b,c = load_gamemode_gametype (a)
