#from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
class Windows(tk.Frame):
    def __init__(self,title, colorFont,x,y,function):
        #tk.Tk.__init__(self, windows, width=x, height=y, bg=colorFont, **kwargs)
        #self.pack_propagate(0)
        self.windows=tk.Tk()
        super().__init__(self.windows)        
        self.color = colorFont
        self.configure(bg=colorFont)
        self.width=x
        self.height=y   
        self.pack(fill='both')
        self.ws = self.windows.winfo_screenwidth()
        self.hs = self.windows.winfo_screenheight()
        self.widthCenter = (self.ws/2) - (self.width/2)
        self.heightCenter = (self.hs/2) - (self.height/2)
        

        if (self.width==0 and self.height==0):
            self.windows.geometry(str(self.ws) + "x" + str(self.hs) )

        else :
            self.windows.geometry(str(self.width) + "x" + str(self.height) + "+" + str(int(self.widthCenter)) + "+" +str(int(self.heightCenter)))

        self.windows.title(title)
        self.function=lambda: function()
        self.windows.protocol("WM_DELETE_WINDOW",self.on_closing )


    def on_closing(self):
            
            if(self.function != None):
                #self.windows.destroy()
                self.function()
            else :
                self.windows.destroy()


def exit():

    if(messageAskyesno("Quit", "Do you want to quit?")):
            sys.exit()  
    else:
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
    