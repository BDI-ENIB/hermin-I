import Config
import logging
import time
logging.basicConfig(filename=Config.LOG_FILE,level=logging.INFO)
logging.info(str(time.strftime('%Hh' '%M' ' %S')) + ' Start Dolmen')
while 1:
    Config.home_Function(None)
