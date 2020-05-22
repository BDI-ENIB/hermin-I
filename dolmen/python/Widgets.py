#from tkinter import *
import tkinter as tk
import Windows
from PIL import Image, ImageTk
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import sys
import time

def addImage(windows,myphoto,colorFont,row,column):

    photo = tk.PhotoImage(file=myphoto,master=windows)
    canvas = tk.Canvas(windows,width=photo.width(), height=photo.height(),bg = 'white')
    canvas.create_image(0, 0, anchor="nw", image=photo)
    canvas.grid(row=row, column=column)
    canvas.image=photo
    windows.mainloop()


class Widgets():

    def __init__(self,windows, title,colorFont,colorText,row,column):
        
        self.windows=windows
        self.title=title
        self.colorFont=colorFont
        self.colorText=colorText
        self.row=row
        self.column=column


class ButtonDisplay(Widgets):

    def __init__(self,windows, title,colorFont,colorText,colorSelect,function,x,y,row,column):

        Widgets.__init__(self,windows,title,colorFont,colorText,row,column)              
        self.x=x
        self.y=y
        self.windows = windows
        self.function=function 
        self.colorSelect=colorSelect      
        self.button= tk.Button(self.windows,anchor="center",text=self.title, bg=self.colorFont,fg=self.colorText,activebackground=self.colorSelect,command=self.function)
        self.button.grid(row=self.row, column=self.column)   
        self.button.config( width = self.x, height = self.y )


    def enable(self):
        self.button.config(state=tk.NORMAL)


    def disable(self):
        self.button.config(state=tk.DISABLED)
    
    def getState(self):
        return self.button['state']


class TextInput(Widgets):

    def __init__(self,windows, title,colorFont,colorText,rowText,columnText,rowInput,columnInput):

        Widgets.__init__(self,windows,title,colorFont,colorText,rowInput,columnInput)
        self.entry=tk.StringVar()
        self.default = "texte par défaut"
        self.rowText=rowText
        self.columnText=columnText
        if(self.title!=None):
            self.windows.message = tk.Label(self.windows, bg=self.colorFont,fg=self.colorText,text=self.title)
            self.windows.message.grid(row=self.rowText, column=self.columnText)   
        self.StringText = tk.Entry(self.windows,bg=self.colorFont,fg=self.colorText,textvariable=self.entry)
        self.entry.set(self.default)
        self.StringText.grid(row=self.row, column=self.column)   

    def getEntry(self):

        if (self.StringText):
            data = str(self.StringText.get())
            #print(data)
            return data

class Case(Widgets):

    def __init__(self,windows, title,colorFont,colorText,colorSelect,function,row,column,default):

        Widgets.__init__(self,windows,title,colorFont,colorText,row,column)
        self.state=tk.StringVar()
        self.function=function
        self.colorSelect=colorSelect
        #self.default=0
        self.default=default
        self.case = tk.Checkbutton(self.windows, text=self.title, bg=self.colorFont,fg=self.colorText,activebackground=self.colorSelect,variable=self.state,command=self.function)
        self.state.set(self.default)
        self.case.grid(row=self.row, column=self.column) 


    def getState(self):

        print(self.state.get())
        return self.state.get()


    def enable(self):
        self.button.config(state=tk.NORMAL)   
        

    def disable(self):
        self.button.config(state=tk.DISABLED) 

class DropdownList(Widgets):

    def __init__(self,windows, title, dropdownList,colorFont,colorText,row,column):

        Widgets.__init__(self,windows,title,colorFont,colorText,row,column)
        self.dropdownList=dropdownList
        self.default=1
        self.listbox = tk.Listbox(self.windows, bg=self.colorFont,fg=colorText)

        for i in range(0,len(self.dropdownList)):
            self.listbox.insert(tk.END,self.dropdownList[i])

        self.listbox.activate(self.default)
        self.listbox.selection_set( first = self.default )
        self.listbox.grid(row=self.row, column=self.column)


    def getChoose(self):

        print(self.listbox.get(tk.ACTIVE))
        return self.listbox.get(tk.ACTIVE)


class TextToPrint(Widgets):

    def __init__(self,windows, title,colorFont,colorText,row,column):

        Widgets.__init__(self,windows,title,colorFont,colorText,row,column)
        self.windows.message = tk.Label(self.windows, bg=self.colorFont, fg=self.colorText,text=self.title)
        self.windows.message.grid(row=self.row, column=self.column) 


class timeDisplay(Widgets):

    def __init__(self,windows, title,colorFont,colorText,row,column):

        Widgets.__init__(self,windows,title,colorFont,colorText,row,column)
        self.windows.message = tk.Label(self.windows, bg=self.colorFont, fg=self.colorText,text="")        
        self.windows.message.grid(row=self.row, column=self.column)
        self.now = time.strftime("%H:%M:%S")


    def update_clock(self):
        self.now = time.strftime("%H:%M:%S")
        self.windows.message.configure(text=self.now)       



