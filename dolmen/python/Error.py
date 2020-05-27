import logging
import Dolmen
import time

class ErrorLog():

    def __init__(self,name,typeLog):
        self.name=name
        self.typeLog=typeLog
        logging.basicConfig(filename=self.name,filemode='w',level=self.typeLog)

    def InfoSaveLog(self,typeError,text): # Save message in log 
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
