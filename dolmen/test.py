from tkinter import *
import tkinter.font as font

class Window:
    def __init__(self):
        root = Tk()
        #print(font.families())  # print list of what's available
        root.title("Serial Connection Program")
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(size=48)
        self.mainFrame = Frame(root)
        self.mainFrame.pack()

        def_font=font.Font(family='Times')
        self.portLabel = Label(self.mainFrame, text="Port1: ", font=def_font)
        self.portLabel.pack()

        my_font=font.Font(family='Arial')
        self.portLabel = Label(self.mainFrame, text="Port2: ", font=my_font)
        self.portLabel.pack()

        root.mainloop()

win = Window()