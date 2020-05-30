#import python Module
import logging
import time
#import Dolmen Module
import Dolmen


class ErrorLog():

    def __init__(self,name,typeLog):

        #name to write in log
        self.name=name

        #log type
        self.typeLog=typeLog

        #create log
        logging.basicConfig(filename=self.name,filemode='w',level=self.typeLog)

    # function to save message in log
    def InfoSaveLog(self,typeError,text):  
        # Save in log (depending of error type)
        if typeError =="info":
            logging.info(Dolmen.currentTime() + " " + text)
            return

        if typeError=="warning":
            logging.warning(Dolmen.currentTime() + " " + text)
            return

        if typeError=="error":
            logging.error(Dolmen.currentTime() + " " + text)
            return

        if typeError=="critical":
            logging.critical(Dolmen.currentTime() + " " + text)
            return

        if typeError=="debug":
            logging.debug(Dolmen.currentTime() + " " + text)
            return

        else:
            print("Problem : error not found")
            logging.error(Dolmen.currentTime() + " error " + text + " not found")
            return
