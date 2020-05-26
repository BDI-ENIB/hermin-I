#Import modules:

import Windows
import Widgets
import Graph
import Dolmen
import Sensors
import csv
import logging
import time
from matplotlib.animation import FuncAnimation
import sys

#LOG_TYPE => level of log (default INFO)
#exemple: LOG_TYPE="DEBUG" or LOG_TYPE=logging.DEBUG
"""
LOG_TYPE="INFO"
PATH = "/home/axeln/hermin-I/dolmen/python"
NAME = "report.csv"
UPDATE_DELAY = 1000
LOG_FILE = 'dolmen.log'
SAVE_REPORT_FOLDER = "report generation"
"""
THEME="normal"
LOG_TYPE=None
PATH = None
NAME = None
UPDATE_DELAY = None
LOG_FILE = None
SAVE_REPORT_FOLDER = None
TIME_FOLDER=Dolmen.currentTime()
NAME_SAVE_FOLDER = str(time.strftime('%Y_' '%m_' '%d_'))+str(TIME_FOLDER)

#figure name file whe, rapport generation
NAME_SAVE_FIGURE = 'report.png'
# name logo in About windows
NAME_ABOUT_IMAGE = "logos.png"
#Windows color
colorFont = None
colorText = None
colorSelect = None
xColor = None
yColor = None
axeLabelColor = None
gridColor = None
facecolor2d = None
facecolor3d = None
graphLegend = None

if THEME == "normal":
    colorFont = "white"
    colorText = "black"
    colorSelect = "grey"
    xColor = "black"
    yColor = "black"
    axeLabelColor = "black"
    gridColor = "black"
    facecolor2d = "white"
    facecolor3d = "white"
    graphLegend = "white"

if THEME == "dark":
    colorFont = "black"
    colorText = "white"
    colorSelect = "grey"
    xColor = "white"
    yColor = "white"
    axeLabelColor = "white"
    gridColor = "white"
    facecolor2d = "grey"
    facecolor3d = "grey"
    graphLegend = "black"

#My figure creation
# for row and colum in figure 0->value
figure=Graph.Graph(20,8,3,4,[4,4,4,2],[4,2,2],colorText,xColor,yColor,axeLabelColor,gridColor,colorFont)
myFigure = figure.figure
f1= Graph.GraphPlot(figure,figure.grid[1, 0:3],"Temperator","time","Temperator (°c)",[-55, 55],facecolor2d,graphLegend,"left")
f2= Graph.GraphPlot(figure,figure.grid[2, 0:3],"Pression","time","Pression (Pascal)",[-110000, 110000],facecolor2d,graphLegend,"left")
f3= Graph.Graph3d(figure,figure.grid[0, 0],"Acceleration","x (ms-2)","y (ms-2)","z (ms-2)",(-10,10),(-10,10),(-10,10),False,facecolor3d,graphLegend)
f4= Graph.Graph3d(figure,figure.grid[0, 1],"Gyroscope","x (ms-2)","y (ms-2)","z (ms-2)",(-10,10),(-10,10),(-10,10),False,facecolor3d,graphLegend)
f5= Graph.Graph3d(figure,figure.grid[0, 2],"GPS","x","y","z",(-1000,1000),(-1000,1000),(-1000,1000),True,facecolor3d,graphLegend)
f6= Graph.GraphHist(figure,figure.grid[0:3, 3],"Altitude","","Altitude (m)",[0, 5000],facecolor2d,"right")

#sensors Creation
temp1=Sensors.Sensors("temperature (Â°c)",4,0,"2d",f1,"Sensor 1","blue")
temp2=Sensors.Sensors("temperature (Â°c)",5,1,"2d",f1,"Sensor 2","red")
pressure1=Sensors.Sensors("pressure (Pa)",6,0,"2d",f2,"Sensor 1","red")
pressure2=Sensors.Sensors("pressure (Pa)",7,1,"2d",f2,"Sensor 2","green")
altitude=Sensors.Sensors("altitude (m)",8,0,"hist",f6,"Sensor 1","red")
acc = Sensors.Sensors(["accelerometer_X (ms-2)","accelerometer_Y (ms-2)","accelerometer_Z (ms-2)"],2,0,"3d",f3,'o','black')
gyro = Sensors.Sensors(["gyroscope_X (ms-2)","gyroscope_Y (ms-2)","gyroscope_Z (ms-2)"],3,0,"3d",f4,'o','black')
#altitude2=Sensors.Sensors("altitude (m)",10,1,"hist",f6,"2S","green")
#altitude3=Sensors.Sensors("altitude (m)",11,2,"hist",f6,"3S","black")
#altitude4=Sensors.Sensors("altitude (m)",12,3,"hist",f6,"4S","grey")

#create sensors list
sensors = [temp1,temp2,pressure1,pressure2,acc,gyro,altitude]
#sensor=[]
def home_Function(last_windows):
    #destroy the last windows (if there is one)
    if(last_windows!=None):
        last_windows.windows.destroy()
    
    logging.info(Dolmen.currentTime() + ' Entering in home mode')
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
    
    logging.info(Dolmen.currentTime() + ' Entering in admin mode')
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
    
    logging.info(Dolmen.currentTime() + ' Entering in sensor management')
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
    
    logging.info(Dolmen.currentTime() + ' Entering in add sensor mode')
    #Create the add_sensor_interface windows
    add_sensor_interface = Windows.Windows("Add Sensors",colorFont,220,100,lambda:sensors_management_Function(add_sensor_interface),3,3)
    
    #Enter class Name
    sensor_add_name = Widgets.TextInput(add_sensor_interface,"Sensor name : ",colorFont,colorText,1,2,2,2)
    #Widgets.TextToPrint(add_sensor_interface,"",None,colorFont,colorText)
    
    #Saving Button
    add_sensor_save_button = Widgets.ButtonDisplay(add_sensor_interface,"Save",colorFont,colorText,colorSelect,lambda :Dolmen.add_sensor_save_Function(add_sensor_interface,sensor_add_name),20,3,3,2)
    
    Widgets.TextToPrint(add_sensor_interface,"      ",colorFont,colorText,1,1)
    Widgets.TextToPrint(add_sensor_interface,"      ",colorFont,colorText,1,3)
    
    #update the add_sensor_interface windows
    add_sensor_interface.windows.update()

    add_sensor_interface.windows.mainloop()
    #add_sensor_interface.destroy()



def about_Function(last_windows):

    #destroy the last windows (if there is one)
    if(last_windows!=None):
        last_windows.windows.destroy()
    
    logging.info(Dolmen.currentTime() + ' Entering in about team')
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
    
    if Dolmen.fileExist(NAME_ABOUT_IMAGE):
        Widgets.addImage(about_interface,NAME_ABOUT_IMAGE,colorFont,4,1)
    else :
        logging.warning(Dolmen.currentTime() + ' no found image file for about windows')
        print("no found image file for about windows")

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

    logging.info(Dolmen.currentTime() + ' Entering in choose fire mode')
    Dolmen.clearFigure();    
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

    logging.info(Dolmen.currentTime() + ' Entering in offline mode')
    #import data
    if Windows.askopenfilename(figure,PATH):
        print(figure.file)
        #Creating fire_interface windows
        fire__offline_interface = Windows.Windows("Fire Mode",colorFont,0,0,lambda:choose_fire_mode(fire__offline_interface),3,9) 
        
        #Adding graph  
        figure.addToWindows(fire__offline_interface,1,1,8,2,9)  
        
        start_button = None
        stop_button = None
        
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
        ani = FuncAnimation(myFigure, Dolmen.updateOnline,fargs = (start_button,stop_button), frames=100, interval=UPDATE_DELAY, repeat=False) #or ani = FuncAnimation(plt.gcf(), update, 200)
        fire__offline_interface.windows.mainloop()
        #fire__offline_interface.destroy()

    else :
        logging.warning(Dolmen.currentTime() + ' No file chosen')
        Windows.messageShowwarning("Open Filename", "Warning, you must choose a file ")
        choose_fire_mode(None)

def fire_Function_online(last_windows):
    Windows.messageShowinfo("Developpment Info", "Online mode is in developpment ") 
    
    
    #destroy the last windows (if there is one)
    if(last_windows!=None):
        last_windows.windows.destroy()
    
    # add CSV file to figure
    figure.file = NAME
    
    if Dolmen.fileExist(figure.file)==True: # verif if there is the csv file
        print(figure.file)
        logging.info(Dolmen.currentTime() + ' Entering in online mode')
        #Creating fire_interface windows
        
        fire__online_interface = Windows.Windows("Fire Mode",colorFont,0,0,lambda:choose_fire_mode(fire__online_interface),4,9) 
            
        #Adding graph  
        figure.addToWindows(fire__online_interface,1,1,8,4,7)  

        start_button = None
        stop_button = None

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
        

        #updating graph     
        ani = FuncAnimation(myFigure, Dolmen.updateOnline,fargs = (start_button,stop_button), frames=100, interval=UPDATE_DELAY, repeat=False) #or ani = FuncAnimation(plt.gcf(), update, 200) 
        

        fire__online_interface.windows.mainloop()
        #fire__offline_interface.destroy()
    else :
        Windows.messageShowwarning("Open Filename", "CSV file no found")
        logging.info(Dolmen.currentTime() + ' CSV file no found')
        choose_fire_mode(None)

    
