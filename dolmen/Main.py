import Config
import Error
import Dolmen
import sys


#verifing if there is argument    
if len(sys.argv)==1 :
    print("no argument given")
    sys.exit()

else:
    Config.LOG_TYPE=str(sys.argv[1])
    Config.PATH = str(sys.argv[2])
    Config.NAME = str(sys.argv[3])
    Config.UPDATE_DELAY = int(sys.argv[4])
    Config.LOG_FILE = str(sys.argv[5])
    Config.SAVE_REPORT_FOLDER = str(sys.argv[6])
    Config.CSV = str(sys.argv[7])
    Config.NAME_SAVE_FIGURE=str(sys.argv[8])
    Config.CONFIG_TXT=str(sys.argv[9])
    Config.THEME=str(sys.argv[10])
    Config.ROCKET_NAME=str(sys.argv[11])

try:
    Config.Log=Error.ErrorLog(Config.LOG_FILE,Config.LOG_TYPE)
   
except:
    Config.Log=Error.ErrorLog(Config.LOG_FILE,"info")
    Config.Log.InfoSaveLog("warning",'logging level error adding default INFO')
    print("logging level error adding default INFO")
    
Config.Log.InfoSaveLog("info",'Start Dolmen')   

while 1 :
    Config.home_Function(None)
