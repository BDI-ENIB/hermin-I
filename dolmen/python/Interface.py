from tkinter import *
import Windows
import Widgets
fire_mode=None
admin_mode=None
def home():
    global fire_mode, admin_mode
    fire_mode = Tk()
    fire_mode_interface = Windows.Windows(fire_mode,"Welcome",1000,1000)
    Widgets.TextToPrint(fire_mode_interface,"DOLMEN Alpha version",None)
    admin_mode_button = Widgets.ButtonDisplay(fire_mode_interface,"Admin Mode","right","black",admin,50,50)
    fire_mode_button = Widgets.ButtonDisplay(fire_mode_interface,"Fire Mode","left","black",None,50,50)
    about_button = Widgets.ButtonDisplay(fire_mode_interface,"About","bottom","black",None,50,50)
    fire_mode_interface.mainloop()
    fire_mode_interface.destroy()



def admin():
    global fire_mode, admin_mode
    fire_mode.destroy()
    admin_mode = Tk()
    admin_mode_interface = Windows.Windows(admin_mode,"Administrator",1000,1000)
    Widgets.TextToPrint(admin_mode_interface,"Administrator Mode",None)
    test = Widgets.TextInput(admin_mode_interface,"test",None)
    test2=Widgets.Case(admin_mode_interface,"test",None,None)
    test3 = Widgets.TextInput(admin_mode_interface,"test3",None)
    tab= ["test1","test2","test3"]
    Widgets.DropdownList(admin_mode_interface,"title",None,tab)
    Widgets.TextToPrint(admin_mode_interface,"test display : uidhfgfhevbdgubgdirbht",None)
    """
    var_choix = StringVar()
    choix_rouge = Radiobutton(admin_mode, text="Rouge", variable=var_choix, value="rouge")
    choix_vert = Radiobutton(admin_mode, text="Vert", variable=var_choix, value="vert")
    choix_bleu = Radiobutton(admin_mode, text="Bleu", variable=var_choix, value="bleu")
    choix_rouge.pack()
    choix_vert.pack()
    choix_bleu.pack()
    print(var_choix.get())
    """
    admin_mode_interface.mainloop()
    admin_mode_interface.destroy()

