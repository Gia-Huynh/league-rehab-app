import configparser
config = configparser.ConfigParser()
config.read("params.ini")
from datetime import date, datetime
now = datetime.now()
print (now.weekday())
