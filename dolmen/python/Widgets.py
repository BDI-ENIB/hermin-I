#from tkinter import *
import tkinter as tk
import Windows
from PIL import Image, ImageTk
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import sys
import time

"""
def addFrame(windows,position):

    MyFrame = tk.Frame(windows, borderwidth=2, relief=GROOVE)
    MyFrame.pack(side=position, padx=500, pady=500)
    windows.mainloop()
    return MyFrame
"""

def addImage(windows,myphoto,position,colorFont):

    photo = tk.PhotoImage(file=myphoto,master=windows)
    canvas = tk.Canvas(windows,width=photo.width(), height=photo.height(),bg = 'white')
    canvas.create_image(0, 0, anchor="nw", image=photo)
    canvas.pack(side=position)
    canvas.image=photo
    windows.mainloop()


class Widgets():

    def __init__(self,windows, title,position,colorFont,colorText):
        
        self.windows=windows
        self.title=title
        self.position=position
        self.colorFont=colorFont
        self.colorText=colorText


class ButtonDisplay(Widgets):

    def __init__(self,windows, title,position,colorFont,colorText,colorSelect,function,x,y):

        Widgets.__init__(self,windows,title,position,colorFont,colorText)              
        self.x=x
        self.y=y
        self.windows = windows
        self.function=function 
        self.colorSelect=colorSelect      
        self.button= tk.Button(self.windows,anchor="center",text=self.title, bg=self.colorFont,fg=self.colorText,activebackground=self.colorSelect,command=self.function)   
        self.button.config( width = self.x, height = self.y )

        if(position!=None):            
            self.button.pack(side=self.position)


    def enable(self):
        self.button.config(state=tk.NORMAL)   


    def disable(self):
        self.button.config(state=tk.DISABLED)     
    
    
    def getState(self):
        print(self.button['state'])


class TextInput(Widgets):

    def __init__(self,windows, title, position,colorFont,colorText):

        Widgets.__init__(self,windows,title,position,colorFont,colorText)
        self.entry=tk.StringVar()
        self.default = "texte par défaut"
        if(self.title!=None):
            self.windows.message = tk.Label(self.windows, bg=self.colorFont,fg=self.colorText,text=self.title)
            if(self.position == None):
                self.windows.message.pack()
            else :
                self.windows.message.pack(side = self.position)
        self.StringText = tk.Entry(self.windows,bg=self.colorFont,fg=self.colorText,textvariable=self.entry)
        self.entry.set(self.default)
        self.StringText.pack(side=self.position)


    def getEntry(self):

        if (self.StringText):
            data = str(self.StringText.get())
            #print(data)
            return data

class Case(Widgets):

    def __init__(self,windows, title, position, function,colorFont,colorText,colorSelect):

        Widgets.__init__(self,windows,title,position,colorFont,colorText)
        self.state=tk.StringVar()
        self.function=function
        self.colorSelect=colorSelect
        self.default=0
        case = tk.Checkbutton(self.windows, text=self.title, bg=self.colorFont,fg=colorText,activebackground=colorSelect,variable=self.state,command=self.function)
        self.state.set(self.default)
        case.pack(side=self.position)    


    def getState(self):

        print(self.state.get())
        return self.state.get()


    def enable(self):
        self.button.config(state=tk.NORMAL)   
        

    def disable(self):
        self.button.config(state=tk.DISABLED) 

class DropdownList(Widgets):

    def __init__(self,windows, title, position, dropdownList,colorFont,colorText):

        Widgets.__init__(self,windows,title,position,colorFont,colorText)
        self.dropdownList=dropdownList
        self.default=1
        self.listbox = tk.Listbox(self.windows, bg=self.colorFont,fg=colorText)

        for i in range(0,len(self.dropdownList)):
            self.listbox.insert(tk.END,self.dropdownList[i])

        self.listbox.activate(self.default)
        self.listbox.selection_set( first = self.default )
        self.listbox.pack(side=self.position)


    def getChoose(self):

        print(self.listbox.get(tk.ACTIVE))
        #print(self.listbox.curselection())
        return self.listbox.get(tk.ACTIVE)


class TextToPrint(Widgets):

    def __init__(self,windows, title, position,colorFont,colorText):

        Widgets.__init__(self,windows,title,position,colorFont,colorText)
        self.windows.message = tk.Label(self.windows, bg=self.colorFont, fg=self.colorText,text=self.title)
        self.windows.message.pack(side=self.position) 


class timeDisplay(Widgets):

    def __init__(self,windows, title, position,colorFont,colorText):

        Widgets.__init__(self,windows,title,position,colorFont,colorText)
        self.windows.message = tk.Label(self.windows, bg=self.colorFont, fg=self.colorText,text="")        
        self.windows.message.pack(side=self.position)
        self.now = time.strftime("%H:%M:%S")


    def update_clock(self):
        self.now = time.strftime("%H:%M:%S")
        self.windows.message.configure(text=self.now)        
        #self.windows.message.after(200, self.update_clock)



