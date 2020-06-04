#import python Module
import os
import os.path
import csv
import time
import shutil

#import Dolmen Module
import Windows
import Widgets
import Graph
import Config
import Sensors
import Error

count=0 # current line in CSV
state_communication=False #if True => start decoding

def currentTime(): # return the current time
    return str(time.strftime('%H.' '%M.' '%S'))


def currentDate(): # return the current date
    return str(time.strftime('%Y_' '%m_' '%d_'))


def decodingCSV(): #open and decoding CSV file
    global count
    #import csv 
    filename = open(Config.CSV, 'r', encoding='latin1')          
    reader = csv.reader(filename, delimiter=';')    
    lines = [line for line in reader] #import list of CSV lines
    filename.close()
    
    # add and find the CSV line to decode

    if lines==[] and count==0: #if CSV is empty
        return

        
    if (len(lines)>count):
        if lines[count]==['stop']:
            state_set_communication(Config.start_button,Config.stop_button,False,Config.currentMode,Config.figure.file,False)

        #find time
        for j in range(0,len(lines[count])-1):            
                        
            if str(lines[count][j])=='0' and str(lines[count][j+1])=='time (s)': # time sensor detected    
                    
                if str(lines[count][j+2])!="": # if time data not empty
                    for sensor in Config.sensors_list_set_time:
                        sensor.x.append(float(lines[count][j+2]))
            
        #decoding current line for each sensors 
        for sensor in Config.sensors:
                sensor.decoding(lines[count])

        #verifing if all sensors has been treated
        for sensor in Config.sensors:
                sensor.verifing()   
                
        #update line        
        count+=1
    else:
        return
    

def fileExist(fileToTest): # detect if file in folder exist

    try:
        with open(fileToTest,'r',encoding='latin1') as filename:            
            return  True #file exist

    except: #no file
        Config.Log.InfoSaveLog("warning",str(fileToTest + "not exist"))       
        return False # return error file no found


def updateOffline(i,start_button,stop_button): # decoding csv and updating graph in Offline mode
    global state_communication

    if(state_communication==True and fileExist(Config.figure.file)==True): #if you click on the start button of fire_interface windows and csv name exist
        decodingCSV() # decoding csv

        if(state_communication==True and fileExist(Config.figure.file)==True): 
            for sensor in Config.sensors:
                sensor.graph.animate()# update graph   

    else : #if no CSV file
        if fileExist(Config.figure.file)==False :
            Windows.messageShowwarning("Open Filename", "Corrupted CSV file or not found")
            Config.Log.InfoSaveLog("info",'Corrupted CSV file or not found')
    

def updateOnline(i,start_button,stop_button): # decoding csv and updating graph in Online mode
    global state_communication

    if(state_communication==True ): #if you click on the start button of fire_interface windows and csv name exist
        decodingCSV() # decoding csv
        
        for sensor in Config.sensors:
            sensor.graph.animate()# update graph 

    else :#if no CSV file
        if fileExist(Config.figure.file)==False :
            Windows.messageShowwarning("Open Filename", "Corrupted CSV file or not found")
            Config.Log.InfoSaveLog("info",'Corrupted CSV file or not found')
    
                           
def initFigure(): #init and reset graph
    global count,state_communication

    #disable communication
    state_communication = False
    #reset current line in CSV
    count=0
    #reset CSV file
    os.remove(Config.CSV)
    filename = open(Config.CSV, 'w')
    filename.close()

    #init each graphe
    for sensor in Config.sensors:
        sensor.graph.initGraph()
                
def report_Function(): #report generation
    global state_communication,save

    if (state_communication == False): # if decoding is stopped

        #check if is save folder exist       
        if not os.path.exists(Config.SAVE_REPORT_FOLDER):
            Config.Log.InfoSaveLog("error",str(Config.SAVE_REPORT_FOLDER + " folder not found => creation"))            
            os.makedirs(Config.SAVE_REPORT_FOLDER)

        if not os.path.exists(Config.SAVE_REPORT_FOLDER + '/'+ str(Config.NAME_SAVE_FOLDER)):
            Config.Log.InfoSaveLog("error",str(Config.NAME_SAVE_FOLDER + " folder not found => creation"))
            os.makedirs(Config.SAVE_REPORT_FOLDER + '/'+ str(Config.NAME_SAVE_FOLDER))

        #save report
        shutil.copy(Config.figure.file,Config.SAVE_REPORT_FOLDER + '/'+ str(Config.NAME_SAVE_FOLDER) + '/' )
        shutil.copy(Config.CSV,Config.SAVE_REPORT_FOLDER + '/'+ str(Config.NAME_SAVE_FOLDER) + '/' ) #copy csv file in save report folder        
        Config.figure.saveFig(Config.SAVE_REPORT_FOLDER,Config.NAME_SAVE_FOLDER,Config.NAME_SAVE_FIGURE) #save figure in save report folder
        Windows.messageShowinfo("Report generation","Report generation successfully created.")

        #print and save in log
        Config.Log.InfoSaveLog("info",str("report generation in " + Config.SAVE_REPORT_FOLDER + "/" + Config.NAME_SAVE_FOLDER))
        print("report generation in   " + Config.SAVE_REPORT_FOLDER + "/" + Config.NAME_SAVE_FOLDER)

    else : # if decoding is not stopped 
        #print and save in log 
        Windows.messageShowwarning("Report generation warning","Warning : please stop the data receive before to generate the report.")
        Config.Log.InfoSaveLog("info",str("trying to generate report before stopping decoding"))


def state_set_communication(start_button,stop_button,state,currentMode,frame,askToStop): # mode => true :ask to and start stop decoding, False : start and stop with no ask 
    global state_communication
    
    #if the user click on the start button
    if(state==True):
        #initFigure()
        #enable decoding
        state_communication=True
        Config.Log.InfoSaveLog("info",'start decoding') 

        #communication with c++
        config=open(Config.CONFIG_TXT, "w")
        config.write("true")
        config.write("\n")
        config.write(str(currentMode))
        config.write("\n")
        config.write(frame)
        config.close()  

        #set button start ans stop state
        #disable start button
        start_button.disable()
        #enable stop button
        stop_button.enable()      

    #if the user click on the stop button
    elif(state==False):

        #check if ask stop decoding if true ask confirmation
        if askToStop== True:
            if (Windows.messageAskyesno("End of data receive", "Do you want to stop the data receive ?")):
                Config.Log.InfoSaveLog("info",'stop decoding')
                #enable stop button
                start_button.disable()
                #disable stop button
                stop_button.disable()
                print("stop decoding")
                

        #disable decoding
        state_communication=False

        #communication with c++
        config=open(Config.CONFIG_TXT, "w")
        config.write("false")
        config.write("\n")
        config.write(str(currentMode))

        if askToStop == True:
            Windows.messageShowinfo("","Don't forget to gererate\nreport if you want")

        if askToStop==False :
            print("end CSV file")
            Config.Log.InfoSaveLog("info","end CSV file")

            #disable start button
            start_button.disable()
            #disable stop button
            stop_button.disable()

            Windows.messageShowinfo("","End CSV file\nDon't forget to gererate\nreport if you want")
        
def add_sensor_save_Function(add_sensor_interface,sensor_add_name):
    
    save_condition = True

    if(sensor_add_name.getEntry()==""): #if no name given
        Config.Log.InfoSaveLog("warning",'add new sensor : no name given')
        Windows.messageShowerror("Name error","Please enter the sensor's name")
        save_condition=False

    #check that the sensor does not already exist
    if(os.path.isfile(sensor_add_name.getEntry().lower() + ".hpp") or os.path.isfile(sensor_add_name.getEntry().lower() + ".cpp")):
        Config.Log.InfoSaveLog("warning",str('sensor name ' + sensor_add_name.getEntry().lower() +' already exit'))
        Windows.messageShowerror("Name error",sensor_add_name.getEntry().lower() + " sensor already exist. Please change the sensor's name")
        save_condition=False
    
    
    #if no error, create the hpp and the cpp    
    if(save_condition==True):
        # Creation of sensor.hpp
        hpp = open(sensor_add_name.getEntry().lower() + ".hpp", "x")            
        hpp.write("#ifndef DOLMEN_"+ sensor_add_name.getEntry().upper() +"_HPP")
        hpp.write("\n#define DOLMEN_" + sensor_add_name.getEntry().upper() +"_HPP 1")
        hpp.write("\n")
        hpp.write("\n#include <string>")
        hpp.write('\n#include "sensor.hpp"')
        hpp.write("\n")
        hpp.write("\nnamespace dolmen")
        hpp.write("\n{")
        hpp.write("\n  class " + sensor_add_name.getEntry().capitalize() + " : public Sensor")
        hpp.write("\n  {")
        hpp.write("\n    public :")
        hpp.write("\n    " + sensor_add_name.getEntry().capitalize() + " (int id, std::string name);")
        hpp.write("\n")
        hpp.write("\n    void decoding(const std::string data) override;")
        hpp.write("\n")
        hpp.write("\n    std::string getColumnIdentifiers() override")
        hpp.write("\n    {")
        hpp.write("\n      return " + '"' + sensor_add_name.getEntry().capitalize() + '"'+ ";")
        hpp.write("\n    }")
        hpp.write("\n")
        hpp.write("\n    int getNbAttr() override")
        hpp.write("\n    {")
        hpp.write("\n      return 3;")
        hpp.write("\n    }")
        hpp.write("\n  };")
        hpp.write("\n}")
        hpp.write("\n")
        hpp.write("\n#endif")      
        hpp.close()
        
        # Creation of sensor.cpp
        cpp = open(sensor_add_name.getEntry().lower() + ".cpp", "x")
        cpp.write('#include "' + sensor_add_name.getEntry().lower() + '.hpp"')
        cpp.write("\n")
        cpp.write("\nnamespace dolmen")
        cpp.write("\n{")
        cpp.write("\n  " + sensor_add_name.getEntry().capitalize() + "::" + sensor_add_name.getEntry().capitalize() + " (int id, std::string name):Sensor{id,name}{}")
        cpp.write("\n")
        cpp.write("\n  void " + sensor_add_name.getEntry().capitalize() +"::decoding(const std::string data)")
        cpp.write("\n  {")
        cpp.write("\n    //insert here the decoding method of your sensor, you can check others sensors to see how we created the previous ones")
        cpp.write("\n  }")
        cpp.write("\n} /* dolmen */")
        cpp.close()

        #print save in log and return
        Config.Log.InfoSaveLog("info",str(' sensor ' + str(sensor_add_name.getEntry()).lower() +" generated"))
        Windows.messageShowinfo("Sensor generation",sensor_add_name.getEntry().lower() + """ sensor generation successfully created. Do not forget to complete the decoding function of this class in the c++ code.
\nfor the python code add a sensor in Config.py and eventually create a graph to display it""")
        #return in sensors management windows
        Config.sensors_management_Function(add_sensor_interface)


