#import python Module
import tkinter as tk
import tkinter.font as tkFont
import time
from PIL import Image, ImageTk
#import Dolmen Module
import Windows
import Dolmen
import Config

#add image in windows
def addImage(windows,myphoto,colorFont,row,column,rowspan,columnspan,xSize,ySize):

    #if image file exist
    if Dolmen.fileExist(myphoto):       
    
        #import image
        image = Image.open(myphoto)
        image=image.resize((xSize,ySize), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image,master=windows)
        #create canva to display image
        canvas = tk.Canvas(windows,width=xSize, height=ySize ,bg = 'white')
        #positioning canva in windows 
        canvas.grid(row=row, column=column,columnspan=columnspan, rowspan=rowspan)
        canvas.create_image(xSize/2,ySize/2,anchor="center", image=image)        

        #add image in canva
        canvas.image=image

        windows.mainloop()

    #if no found image
    else :
        Config.Log.InfoSaveLog("warning",'no found image file for about windows')
        print("no found image file for about windows")

#Main Widgets class
class Widgets():

    def __init__(self,windows,title,colorFont,colorText,row,column,fontSize,fontType,police,rowspan,columnspan):

        #define widget variables  
        #define which windows is the widget      
        self.windows=windows

        #text to print in the widget
        self.title=title

        #set widget color
        self.colorFont=colorFont
        self.colorText=colorText

        #define position in windows
        self.row=row
        self.column=column

        self.police=police
        self.fontSize=fontSize
        self.fontType=fontType
        self.rowspan=rowspan
        self.columnspan=columnspan


class ButtonDisplay(Widgets):

    def __init__(self,windows,title,colorFont,colorText,colorSelect,function,x,y,row,column,fontSize,fontType,police,rowspan,columnspan):

        #call Widget constructor
        Widgets.__init__(self,windows,title,colorFont,colorText,row,column,fontSize,fontType,police,rowspan,columnspan) 

        #define button variables    
        #button size
        self.x=x
        self.y=y
        #function when click on button
        self.function=function 

        #color when passing mouse on the button
        self.colorSelect=colorSelect 

        #create button     
        self.button= tk.Button(self.windows,anchor="center",text=self.title, bg=self.colorFont,fg=self.colorText,activebackground=self.colorSelect,command=self.function,font=(self.police, self.fontSize, self.fontType))

        #config button
        self.button.config( width = self.x, height = self.y )

        #positioning the button in windows 
        self.button.grid(row=self.row, column=self.column,rowspan=self.rowspan,columnspan=self.columnspan)   
     
    #function to enable the button
    def enable(self):
        self.button.config(state=tk.NORMAL)

    #function to disable the button
    def disable(self):
        self.button.config(state=tk.DISABLED) 

    #function to get the button's state   
    def getState(self):
        return self.button['state']


class TextInput(Widgets):

    def __init__(self,windows,title,colorFont,colorText,rowText,columnText,rowInput,columnInput,defaultText,fontSize,fontType,police,rowspan,columnspan):

        #call Widget constructor
        Widgets.__init__(self,windows,title,colorFont,colorText,rowInput,columnInput,fontSize,fontType,police,rowspan,columnspan)

        #define text input variables 
        #text input
        self.entry=tk.StringVar()

        #fefaukt text
        self.defaultText = defaultText

        #position in windows
        self.rowText=rowText
        self.columnText=columnText

        #if there is label to display
        if(self.title!=None):
            
            #create label
            self.windows.message = TextToPrint(self.windows,self.title,self.colorFont,self.colorText,self.rowText,self.columnText,self.fontSize,self.fontType,self.police,rowspan,columnspan)

        #create text input
        self.StringText = tk.Entry(self.windows,bg=self.colorFont,fg=self.colorText,textvariable=self.entry)

        #set default text
        self.entry.set(self.defaultText)

        #positioning the text input in windows 
        self.StringText.grid(row=self.row, column=self.column,rowspan=self.rowspan,columnspan=self.columnspan)   

    #function to get the entry text
    def getEntry(self):
        if (self.StringText):
            return str(self.StringText.get())

class Case(Widgets):

    def __init__(self,windows,title,colorFont,colorText,colorSelect,function,row,column,default,fontSize,fontType,police,rowspan,columnspan):

        #call Widget constructor
        Widgets.__init__(self,windows,title,colorFont,colorText,row,column,fontSize,fontType,police,rowspan,columnspan)

        #define case variables
        #state case
        self.state=tk.StringVar()

        #fonction when clicking on case
        self.function=function

        #color on select
        self.colorSelect=colorSelect

        #default state
        self.default=default

        #create case widget
        self.case = tk.Checkbutton(self.windows, text=self.title, bg=self.colorFont,fg=self.colorText,activebackground=self.colorSelect,variable=self.state,command=self.function,font=(self.police, self.fontSize, self.fontType))

        #define default state
        self.state.set(self.default)
        
        #positioning the case in windows 
        self.case.grid(row=self.row, column=self.column,rowspan=self.rowspan,columnspan=self.columnspan) 

    #function to get the state of the case
    def getState(self):
        return self.state.get()

    #enable case
    def enable(self):
        self.button.config(state=tk.NORMAL)     

    #disable case
    def disable(self):
        self.button.config(state=tk.DISABLED) 

class DropdownList(Widgets):

    def __init__(self,windows,title, dropdownList,colorFont,colorText,row,column,fontSize,fontType,police,rowspan,columnspan):

        #call Widget constructor
        Widgets.__init__(self,windows,title,colorFont,colorText,row,column,fontSize,fontType,police,rowspan,columnspan)

        #define DropdownList variables
        #DropdownList
        self.dropdownList=dropdownList

        #default text select
        self.default=1

        #create DropdownList
        self.listbox = tk.Listbox(self.windows, bg=self.colorFont,fg=colorText,font=(self.police, self.fontSize, self.fontType))

        #insert element in DropdownList
        for i in range(0,len(self.dropdownList)):
            self.listbox.insert(tk.END,self.dropdownList[i])

        #define defaukt select element 
        self.listbox.activate(self.default)
        self.listbox.selection_set( first = self.default )

        #positioning the DropdownList in windows 
        self.listbox.grid(row=self.row, column=self.column,rowspan=self.rowspan,columnspan=self.columnspan)

    #function to get the selected element in DropdownList
    def getChoose(self):
        return self.listbox.get(tk.ACTIVE)


class TextToPrint(Widgets):

    def __init__(self,windows, title,colorFont,colorText,row,column,fontSize,fontType,police,rowspan,columnspan):

        #call Widget constructor
        Widgets.__init__(self,windows,title,colorFont,colorText,row,column,fontSize,fontType,police,rowspan,columnspan)
        #create label
        self.windows.message = tk.Label(self.windows, bg=self.colorFont, fg=self.colorText,text=self.title,font=(self.police, self.fontSize, self.fontType))
            
        #positioning the label in windows 
        self.windows.message.grid(row=self.row, column=self.column,columnspan=self.columnspan, rowspan=self.rowspan) 

class DisplayTime():

    def __init__(self, windows,colorFont,colorText,row,column,fontSize,fontType,police,rowspan,columnspan):

        #call Widget constructor
        Widgets.__init__(self,windows,"",colorFont,colorText,row,column,fontSize,fontType,police,rowspan,columnspan)

        #create label displaying time
        self.labelTime = tk.Label(self.windows, text=str(time.strftime('%Y ' '%m ' '%d ')) + "\n" + str(time.strftime('%H.' '%M.' '%S')), font=(self.police, self.fontSize, self.fontType), width=10,bg=self.colorFont, fg=self.colorText)

        #positioning the label displaying time in windows 
        self.labelTime.grid(row=self.row, column=self.column,rowspan=self.rowspan,columnspan=self.columnspan)

        # start the DisplayTime
        self.labelTime.after(1000, self.refresh_label)

    #fonction to update time
    def refresh_label(self):

        # display the new time
        self.labelTime.configure(text=str(time.strftime('%Y ' '%m ' '%d ')) + "\n" + str(time.strftime('%H.' '%M.' '%S')))

        # request tkinter to call self.refresh after 1s (the delay is given in ms)
        self.labelTime.after(1000, self.refresh_label)
 


