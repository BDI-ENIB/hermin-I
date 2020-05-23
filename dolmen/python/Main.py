import Config
import logging
import Dolmen
import time

try:
    logging.basicConfig(filename=Config.LOG_FILE,filemode='w',level=Config.LOG_TYPE)
   
except:
    logging.basicConfig(filename=Config.LOG_FILE,level=logging.INFO)
    logging.warning(Dolmen.currentTime() + ' logging level error adding default INFO')
    print("logging level error adding default INFO")
    
logging.basicConfig(filename=Config.LOG_FILE,level=Config.LOG_TYPE)
    
logging.info(Dolmen.currentTime() + ' Start Dolmen')
#Config.TIME_FOLDER = Dolmen.currentTime()
while 1:
    Config.home_Function(None)
