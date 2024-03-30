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
#a = load_config_preprocessed ('params.ini')

"""Bad code, deleteing
from datetime import date, datetime
def diff_dates (date1, date2):
    return abs(date2-date1).days
def diff_hours (date1, date2):
    return abs(date2-date1).hour
past = datetime.now()
a = load_config_preprocess ('params.ini')
now = datetime.now()
print (diff_hours(past, now))
"""
