from tkinter import *
class Windows(Frame):
    def __init__(self, windows,title, x,y,**kwargs):
        Frame.__init__(self, windows, width=x, height=y, **kwargs)
        self.pack(fill=BOTH)
        windows.geometry(str(x) + "x" + str(y))
        windows.title(title)
        
    