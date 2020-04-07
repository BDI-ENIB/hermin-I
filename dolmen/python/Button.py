from tkinter import *
import Windows
fire_mode=None
admin_mode=None
def home():
    global fire_mode, admin_mode
    fire_mode = Tk()
    fire_mode_interface = Windows.Windows(fire_mode,"Welcome",1000,1000)
    fire_mode_interface.addLabel("DOLMEN Alpha version")
    fire_mode_interface.addButton("Admin Mode","black","right",admin,50,50)
    fire_mode_interface.addButton("Fire Mode","black","left",None,50,50)
    fire_mode_interface.addButton("About","black","bottom",None,50,50)
    fire_mode_interface.mainloop()
    fire_mode_interface.destroy()



def admin():
    global fire_mode, admin_mode
    fire_mode.destroy()
    admin_mode = Tk()
    admin_mode_interface = Windows.Windows(admin_mode,"Administrator",1000,1000)
    admin_mode_interface.addLabel("Administrator Mode")
    admin_mode_interface.addButton("Graph Management","black","top",None,100,25)
    admin_mode_interface.addButton("Windows Management","black","top",None,100,25)
    admin_mode_interface.addButton("Sensors Management","black","top",None,100,25)
    admin_mode_interface.mainloop()
    admin_mode_interface.destroy()