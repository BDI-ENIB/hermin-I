#import python Module
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import sys
import os.path
import shutil
#import Dolmen Module
import Config
import Dolmen
import Error


class Windows(tk.Frame):
    def __init__(self,title, colorFont,width,height,function,row,column):
        #create the windows
        self.windows=tk.Tk()
        super().__init__(self.windows)  
        #add title
        self.windows.title(title)
        #add color font      
        self.color = colorFont
        self.configure(bg=colorFont)
        #define number of rows and columns in windows
        self.row=row
        self.column = column 
        self.windows.rowconfigure(self.row, weight=2)
        self.windows.columnconfigure(self.column, weight=2)  
        #define size windows
        self.width=width
        self.height=height 
        self.pack(fill='both')
        #screen resolution
        self.ws = self.windows.winfo_screenwidth()
        self.hs = self.windows.winfo_screenheight()
        #define center of windows
        self.widthCenter = (self.ws/2) - (self.width/2)
        self.heightCenter = (self.hs/2) - (self.height/2)
        #position and size of wondows
        if (self.width==0 and self.height==0):
            self.windows.geometry(str(self.ws) + "x" + str(self.hs) )
        else :
            self.windows.geometry(str(self.width) + "x" + str(self.height) + "+" + str(int(self.widthCenter)) + "+" +str(int(self.heightCenter)))        
        #define function when exit
        self.function=lambda: function()
        self.windows.protocol("WM_DELETE_WINDOW",self.on_closing )

    #execute fonction when closing windows
    def on_closing(self):            
            if(self.function != None):
                #self.windows.destroy()
                self.function()
            else :
                self.windows.destroy()

#when you exit of Dolmen
def exit():

    if(messageAskyesno("Quit", "Do you want to quit?")):#if exit
            Config.Log.InfoSaveLog("info",' Exit Dolmen')

            #close c++ code
            config=open(Config.CONFIG_TXT, "w")
            config.write("exit")
            config.close()

            #verifing if save folder exist (to save the log file in)
            if not os.path.exists(Config.SAVE_REPORT_FOLDER):            
                os.makedirs(Config.SAVE_REPORT_FOLDER)                
            if not os.path.exists(Config.SAVE_REPORT_FOLDER + '/' + Config.NAME_SAVE_FOLDER):            
                os.makedirs(Config.SAVE_REPORT_FOLDER + '/' + Config.NAME_SAVE_FOLDER)

            #save log file    
            shutil.copy(Config.LOG_FILE,Config.SAVE_REPORT_FOLDER + '/'+ Config.NAME_SAVE_FOLDER + '/' +  Config.LOG_FILE)
            sys.exit()  

    else: #if no exist : nothing
        return

#Information message box :

def messageShowinfo(title,text):
        messagebox.showinfo(title,text) 
         
#Question message boxes : 

def messageAskquestion(title, text):
    return messagebox.askquestion(title, text)

def messageAskokcancel(title, text):
    return messagebox.askokcancel(title, text)

def messageAskretrycancel(title, text):
    return messagebox.askretrycancel(title, text)

def messageAskyesno(title, text):
    return messagebox.askyesno(title, text)

def messageAskyesnocancel(title, text):
    return messagebox.askyesnocancel(title, text)

#Warning message boxes :

def messageShowwarning(title,text):
    messagebox.showwarning(title, text)

def messageShowerror(title,text):
    messagebox.showerror(title, text)

def askopenfilename(figure,path):
    #file select windows
    filename=filedialog.askopenfilename(title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    #try to open file    
    try:
        with open(filename,'r') as UseFile:
            figure.file = filename
            #file exist
            return True
    except:
        #file no exist or no file chosen
        return False
    
