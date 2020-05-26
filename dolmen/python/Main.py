import Config
import logging
import Dolmen
import time
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

try:
    logging.basicConfig(filename=Config.LOG_FILE,filemode='w',level=Config.LOG_TYPE)
   
except:
    logging.basicConfig(filename=Config.LOG_FILE,level=logging.INFO)
    logging.warning(Dolmen.currentTime() + ' logging level error adding default INFO')
    print("logging level error adding default INFO")
    
logging.basicConfig(filename=Config.LOG_FILE,level=Config.LOG_TYPE)
    
logging.info(Dolmen.currentTime() + ' Start Dolmen')

#Config.TIME_FOLDER = Dolmen.currentTime()

while 1 :
    Config.home_Function(None)
