#Import modules:
import Windows
import Widgets
import Graph
import Dolmen
import csv
import logging
import time
from matplotlib.animation import FuncAnimation

PATH = "/home/axeln/hermin-I/dolmen/python"
NAME = "report.csv"
UPDATE_DELAY = 1000
LOG_FILE = 'dolmen.log'
#Windows color
colorFont = "white"
colorText = "black"
colorSelect = "grey"




def home_Function(last_windows):

    #destroy the last windows (if there is one)
    if(last_windows!=None):
        last_windows.windows.destroy()
    
    #Creating home_interface windows
    home_interface = Windows.Windows("Welcome",colorFont,300,100,Windows.exit,3,3)

    #Adding widgets      
    Widgets.TextToPrint(home_interface,"DOLMEN Alpha version",colorFont,colorText,1,2)    
    fire_mode_button = Widgets.ButtonDisplay(home_interface,"Fire Mode",colorFont,colorText,colorSelect,lambda: choose_fire_mode(home_interface),10,2,2,1)
    about_button = Widgets.ButtonDisplay(home_interface,"About Dolmen",colorFont,colorText,colorSelect,lambda: about_Function(home_interface),15,2,2,2)
    admin_mode_button = Widgets.ButtonDisplay(home_interface,"Administrator Mode",colorFont,colorText,colorSelect,lambda: admin_Function(home_interface),15,2,2,3)
    quit_dolmen_button = Widgets.ButtonDisplay(home_interface,"Quit Dolmen",colorFont,colorText,colorSelect,Windows.exit,10,2,3,2)
    home_interface.windows.mainloop()
    #home_interface.destroy()

def admin_Function(last_windows):

    #destroy the last windows (if there is one)
    if(last_windows!=None):
        last_windows.windows.destroy()
    
    #Creating admin_mode_interface windows
    admin_mode_interface = Windows.Windows("Administrator Mode",colorFont,700,250,lambda: home_Function(admin_mode_interface),1,3)

    #Adding widgets  
    graph_management_button = Widgets.ButtonDisplay(admin_mode_interface,"Graph management",colorFont,colorText,colorSelect,None,25,10,1,1)
    windows_management_button = Widgets.ButtonDisplay(admin_mode_interface,"Windows management",colorFont,colorText,colorSelect,None,25,10,1,2)
    sensors_management_button = Widgets.ButtonDisplay(admin_mode_interface,"Sensor management",colorFont,colorText,colorSelect,lambda: sensors_management_Function(admin_mode_interface),25,10,1,3)
    
    #admin_mode_interface.windows.update()
    admin_mode_interface.windows.mainloop()
    #admin_mode_interface.destroy()


def sensors_management_Function(last_windows):

    #destroy the last windows (if there is one)
    if(last_windows!=None):
        last_windows.windows.destroy()
    
    #Creating sensors_management_interface windows
    sensors_management_interface = Windows.Windows("Sensors management mode",colorFont,700,250,lambda: admin_Function(sensors_management_interface),1,3)

    #Adding widgets     
    sensors_management_add_button = Widgets.ButtonDisplay(sensors_management_interface,"Add new sensor",colorFont,colorText,colorSelect,lambda: add_sensor(sensors_management_interface),25,10,1,1)
    sensors_management_modify_button = Widgets.ButtonDisplay(sensors_management_interface,"Modify sensor",colorFont,colorText,colorSelect,None,25,10,1,2)
    sensors_management_variable_button = Widgets.ButtonDisplay(sensors_management_interface,"Add sensor variable",colorFont,colorText,colorSelect,None,25,10,1,3)


    sensors_management_interface.windows.mainloop()



def add_sensor(last_windows):
    
    #destroy the last windows (if there is one)
    if(last_windows!=None):
        last_windows.windows.destroy()
    
    #Create the add_sensor_interface windows
    add_sensor_interface = Windows.Windows("Add Sensors",colorFont,500,200,lambda:sensors_management_Function(add_sensor_interface),7,5)
    
    #Enter class Name
    sensor_add_name = Widgets.TextInput(add_sensor_interface,"Sensor name : ",colorFont,colorText,1,1,2,1)
    #Widgets.TextToPrint(add_sensor_interface,"",None,colorFont,colorText)
    
    #Enter Argument 1
    sensor_add_arg1 = Widgets.TextInput(add_sensor_interface,"Sensor Argument 1 : ",colorFont,colorText,3,1,4,1)
    sensor_add_arg1_type = Widgets.TextInput(add_sensor_interface,"Type : ",colorFont,colorText,3,2,4,2)
    #Widgets.TextToPrint(add_sensor_interface,"",None,colorFont,colorText)

    #Enter optional Argument 2
    sensor_add_arg2 = Widgets.TextInput(add_sensor_interface,"Sensor Argument 2 : ",colorFont,colorText,3,4,4,4)
    sensor_add_arg2_type = Widgets.TextInput(add_sensor_interface,"Type : ",colorFont,colorText,3,5,4,5)
    #Widgets.TextToPrint(add_sensor_interface,"",None,colorFont,colorText)

    #Enter optional Argument 3
    sensor_add_arg3 = Widgets.TextInput(add_sensor_interface,"Sensor Argument 3 : ",colorFont,colorText,5,1,6,1)
    sensor_add_arg3_type = Widgets.TextInput(add_sensor_interface,"Type : ",colorFont,colorText,5,2,6,2)
    #Widgets.TextToPrint(add_sensor_interface,"",None,colorFont,colorText)

    #Enter optional Argument 4
    sensor_add_arg4 = Widgets.TextInput(add_sensor_interface,"Sensor Argument 4 : ",colorFont,colorText,5,4,6,4)
    sensor_add_arg4_type = Widgets.TextInput(add_sensor_interface,"Type : ",colorFont,colorText,5,5,6,5)
    #Widgets.TextToPrint(add_sensor_interface,"",None,colorFont,colorText)

    #Saving Button
    #Widgets.TextToPrint(add_sensor_interface,"",None,colorFont,colorText)    
    add_sensor_save_button = Widgets.ButtonDisplay(add_sensor_interface,"Save",colorFont,colorText,colorSelect,lambda :Dolmen.add_sensor_save_Function(add_sensor_interface,sensor_add_name, sensor_add_arg1,sensor_add_arg1_type,sensor_add_arg2,sensor_add_arg2_type,sensor_add_arg3,sensor_add_arg3_type,sensor_add_arg4,sensor_add_arg4_type),10,5,7,5)
    Widgets.TextToPrint(add_sensor_interface,"  ",colorFont,colorText,3,3)
    Widgets.TextToPrint(add_sensor_interface,"  ",colorFont,colorText,4,3)
    Widgets.TextToPrint(add_sensor_interface,"  ",colorFont,colorText,5,3)
    Widgets.TextToPrint(add_sensor_interface,"  ",colorFont,colorText,6,3)
    #update the add_sensor_interface windows
    add_sensor_interface.windows.update()

    add_sensor_interface.windows.mainloop()
    #add_sensor_interface.destroy()



def about_Function(last_windows):

    #destroy the last windows (if there is one)
    if(last_windows!=None):
        last_windows.windows.destroy()
    
    #Creating about_interface windows
    about_interface = Windows.Windows("About Dolmen : ",colorFont,1000,600,lambda:home_Function(about_interface),4,1)

    #Adding widgets 
    Widgets.TextToPrint(about_interface,"""
    Timothée Allègre (t7allegr@enib.fr):

    En tant que membre du BDI depuis quelques années, et suivant le projet FUSEX depuis ses débuts, j’ai souhaité m'investir 
    dans ce projet autant que possible. J’ai rapidement tenté de formuler les besoins auxquels une telle interface pourrait 
    répondre, et ai tenté de mettre ma connaissance du projet FUSEX au profit du projet DOLMEN. Je souhaite que ce projet 
    puisse servir non seulement à notre équipe de cette année, mais aussi à d’autres équipes dans le futur, et qu’il puisse 
    vivre quelques années supplémentaires.
    """,colorFont,colorText,1,1)

    Widgets.TextToPrint(about_interface,"""
    Nathan De Saint Just (n6desain@enib.fr):

    En tant que président du BDI depuis 2 ans et fondateur du Pôle KSP au sein de celui-ci avec Evan Roué, Il me tenait à coeur de 
    participer à ce projet que je vois ce développé depuis sa création. Avec grand espoir que tout soit opérationnelle pour la C’space 
    2020 avec le tire de la fusée avec le projet DOLMEN en base sol. Montrer qu’il marche nous permettra de le réutiliser et de la
    partager à tous les autres associations spatiales.
    """,colorFont,colorText,2,1)

    Widgets.TextToPrint(about_interface,"""
    Axel Nougier (a7nougie@enib.fr):

    En tant que membre du BDI depuis quelques années, et suivant le projet Enigma Robotics, j’ai souhaité mettre mes connaissances à 
    profit dans le projet Dolmen afin de découvrir le Pôle KSP. Je souhaite que Dolmen soit un logiciel, simple, mais à la fois 
    robuste et modulable afin qu’il puisse être appliqué à d’autres projets et pouvoir être modifié selon d’autres besoin et être
    amélioré par d’autres personnes.
    """,colorFont,colorText,3,1)
    Widgets.addImage(about_interface,"logos.png",colorFont,4,1)    

    about_interface.windows.mainloop()
    #about_interface.destroy()


def help_fire_mode():

    help_fire_mode = Windows.messageShowinfo("Witch Fire mode you can use ?",
    """
    The Online Fire mode must be use with an emitter to view data in real time 

    The Offline Fire mode must be use when you don't have an emitter or if you want to simulate a rocket launch
    """
    )
   
def help_fire ():

    help_fire = Windows.messageShowinfo("Help Fire mode ?",
    """
    A DEVELOPPER
    """
    )

def choose_fire_mode(last_windows):

    #destroy the last windows (if there is one)
    if(last_windows!=None):
        last_windows.windows.destroy()
        
    #Creating fire_mode_interface windows
    fire_mode_interface = Windows.Windows("Fire Mode Choose",colorFont,350,100,lambda:home_Function(fire_mode_interface),2,3)

    #Adding widgets 
    Widgets.TextToPrint(fire_mode_interface,"Please choose a fire mode :",colorFont,colorText,1,2)
    online_button = Widgets.ButtonDisplay(fire_mode_interface,"Online Mode",colorFont,colorText,colorSelect,lambda:fire_Function_online(fire_mode_interface),10,5,2,1)
    offline_button = Widgets.ButtonDisplay(fire_mode_interface,"Offline Mode",colorFont,colorText,colorSelect,lambda:fire_Function_offline(fire_mode_interface),10,5,2,3)
    help_fire_button = Widgets.ButtonDisplay(fire_mode_interface,"Help",colorFont,colorText,colorSelect,help_fire_mode ,10,5,2,2)
 
    fire_mode_interface.windows.mainloop()


def fire_Function_offline(last_windows): 
    
    #destroy the last windows (if there is one)
    if(last_windows!=None):
        last_windows.windows.destroy()

    logging.info(str(time.strftime('%Hh' '%M' ' %S')) + ' Entering in offline mode')
    #import data
    if Windows.askopenfilename(Dolmen.figure,PATH):
    
        #Creating fire_interface windows
        fire__offline_interface = Windows.Windows("Fire Mode",colorFont,0,0,lambda:choose_fire_mode(fire__offline_interface),3,9) 
        
        #Adding graph  
        Dolmen.figure.addToWindows(fire__offline_interface,1,1,8,2,9)  

        start_button=None
        stop_button=None
        #Adding widgets      
        start_button = Widgets.ButtonDisplay(fire__offline_interface,"Start",colorFont,colorText,colorSelect,lambda:Dolmen.state_set_communication(start_button,stop_button,True),10,10,3,1)
        stop_button = Widgets.ButtonDisplay(fire__offline_interface,"Stop",colorFont,colorText,colorSelect,lambda:Dolmen.state_set_communication(start_button,stop_button,False),10,10,3,5)
        help_fire_button = Widgets.ButtonDisplay(fire__offline_interface,"Help",colorFont,colorText,colorSelect,help_fire,10,5,3,3)
        rapport_button = Widgets.ButtonDisplay(fire__offline_interface,"Generate Rapport",colorFont,colorText,colorSelect,Dolmen.report_Function,15,5,3,4)

        #initial conditions :
            #enable start button
        start_button.enable()

            #disable stop button
        stop_button.disable()

        #updating graph 
        ani = FuncAnimation(Dolmen.myFigure, Dolmen.updateOnline,fargs = (start_button,stop_button), frames=100, interval=UPDATE_DELAY, repeat=False) #or ani = FuncAnimation(plt.gcf(), update, 200)
        fire__offline_interface.windows.mainloop()
        #fire__offline_interface.destroy()

    else : 
        choose_fire_mode(None)

def fire_Function_online(last_windows):
    Windows.messageShowinfo("Developpment Info", "Online mode is in developpment ")
    
    
    #destroy the last windows (if there is one)
    if(last_windows!=None):
        last_windows.windows.destroy()

    
    logging.info(str(time.strftime('%Hh' '%M' ' %S')) + ' Entering in online mode')
    #Creating fire_interface windows
    fire__online_interface = Windows.Windows("Fire Mode",colorFont,0,0,lambda:choose_fire_mode(fire__online_interface),4,9) 
        
    #Adding graph  
    Dolmen.figure.addToWindows(fire__online_interface,1,1,8,4,7)  


    start_button=None
    stop_button=None
    #Adding widgets      
    start_button = Widgets.ButtonDisplay(fire__online_interface,"Start",colorFont,colorText,colorSelect,lambda:Dolmen.state_set_communication(start_button,stop_button,True),10,10,3,1)
    stop_button = Widgets.ButtonDisplay(fire__online_interface,"Stop",colorFont,colorText,colorSelect,lambda:Dolmen.state_set_communication(start_button,stop_button,False),10,10,3,5)
    help_fire_button = Widgets.ButtonDisplay(fire__online_interface,"Help",colorFont,colorText,colorSelect,help_fire,10,5,3,3)
    rapport_button = Widgets.ButtonDisplay(fire__online_interface,"Generate Rapport",colorFont,colorText,colorSelect,Dolmen.report_Function,15,5,3,4)

    #initial conditions :
    #enable start button
    start_button.enable()

    #disable stop button
    stop_button.disable()
    Dolmen.figure.file = NAME

    #updating graph     
    ani = FuncAnimation(Dolmen.myFigure, Dolmen.updateOnline,fargs = (start_button,stop_button), frames=100, interval=UPDATE_DELAY, repeat=False) #or ani = FuncAnimation(plt.gcf(), update, 200) 
    

    fire__online_interface.windows.mainloop()
    #fire__offline_interface.destroy()

    
