from tkinter import *
class Windows(Frame):
    def __init__(self, windows,title, x,y,**kwargs):
        Frame.__init__(self, windows, width=x, height=y, **kwargs)
        self.pack(fill=BOTH)
        windows.geometry(str(x) + "x" + str(y))
        windows.title(title)
        
        
    def addLabel(self,textToPrint):
        self.message = Label(self, text=textToPrint)
        self.message.pack()
        

    def addButton(self, title,color,position,function,x,y):
        self.button= Button(self, text=title, fg=color,command=function)
        self.button.pack(side=position)
        self.button.config( width = x, height = y )

