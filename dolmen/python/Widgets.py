from tkinter import *
import Windows

class Widgets():
    def __init__(self,windows, title,position):
        self.windows=windows
        self.title=title
        self.position=position

class ButtonDisplay(Widgets):
    def __init__(self,windows, title,position,color,function,x,y):
        Widgets.__init__(self,windows,title,position)
        self.color=color
        
        self.function=function
        self.x=x
        self.y=y
        
        self.windows.button= Button(self.windows, text=self.title, fg=self.color,command=self.function)
        self.windows.button.pack(side=self.position)
        self.windows.button.config( width = self.x, height = self.y )

class TextInput(Widgets):
    def __init__(self,windows, title, position):
        Widgets.__init__(self,windows,title,position)
        self.entry=StringVar()
        if(self.title!=None):
            self.windows.message = Label(self.windows, text=self.title)
            self.windows.message.pack()
        StringText = Entry(self.windows,textvariable=self.entry)
        StringText.pack(side=self.position)

    def getEntry():
        if (self.entry):
            return self.entry

class Case(Widgets):
    def __init__(self,windows, title, position, function):
        Widgets.__init__(self,windows,title,position)
        self.state=StringVar()
        self.function=function
        case = Checkbutton(self.windows, text=self.title, variable=self.state,command=self.function)
        case.pack(side=self.position)
    def getState():
        return self.state

class DropdownList(Widgets):
    def __init__(self,windows, title, position, dropdownList):
        Widgets.__init__(self,windows,title,position)
        self.dropdownList=dropdownList
        list = Listbox(self.windows)
        for i in range(0,len(self.dropdownList)):
            list.insert(END,self.dropdownList[i])
        list.pack(side=self.position)

class TextToPrint(Widgets):
    def __init__(self,windows, title, position):
        Widgets.__init__(self,windows,title,position)
        self.windows.message = Label(self.windows, text=self.title)
        self.windows.message.pack(side=self.position)