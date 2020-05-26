import Windows
import Widgets
import Graph
import os.path
import Config
import Sensors
import csv
import time
import logging
import shutil

count=0 # current line in CSV
state_communication=False

def currentTime():
    return str(time.strftime('%H.' '%M.' '%S'))

def decodingCSV():

    global count, state_communication
   
    filename = open(Config.figure.file, 'r', encoding='latin1')
          
    reader = csv.reader(filename, delimiter=';')
    # Data Processing
    lines = [line for line in reader]
    
    if count+1>len(lines):
        state_communication=False
        print("OH SHIT !!!")
        state_communication=False
    else :
        for i in lines[count]:
            line_split=i.split(",")
        #print(line_split) 
        
        for j in range(0,len(line_split)-1):            
                       
            if str(line_split[j])=='0' and str(line_split[j+1])=='time (s)': #time decoding and processing
                
                x=float(line_split[j+2])
                Config.f1.x.append(x)
                Config.f2.x.append(x) 
               
        for sensor in Config.sensors:
                sensor.decoding(line_split)
        for sensor in Config.sensors:
                sensor.verifing()   
                
    #update line        
    count+=1

    filename.close()

def fileExist(fileToTest):
    try:
        with open(fileToTest,'r',encoding='latin1') as filename:
            
            return  True

    except:        
        return False # return error file no found


def updateOffline(i): # decoding csv and updating graph in offline mode

    global state_communication

    if(state_communication==True and fileExist(Config.figure.file)==True): #if you click on the start button of fire_interface windows and csv name exist
        decodingCSV() # decoding csv
        if(state_communication==True and fileExist(Config.figure.file)==True): 
            for sensor in Config.sensors:
                sensor.graph.animate()# update graph
    


def updateOnline(i,start_button,stop_button): # decoding csv and updating graph in Online mode
    global state_communication

    if(state_communication==True ): #if you click on the start button of fire_interface windows and csv name exist
        decodingCSV() # decoding csv
        
        if(state_communication==True):
            for sensor in Config.sensors:
                sensor.graph.animate()# update graph
        
                
    else :
        if fileExist(Config.figure.file)==False :
            Windows.messageShowwarning("Open Filename", "Corrupted CSV file or not found")
            logging.info(currentTime() + ' Corrupted CSV file or not found')
            
     
                
def clearFigure():
    global count,state_communication
    state_communication=False
    count=0
    for sensor in Config.sensors:
        sensor.graph.initGraph()
                
def report_Function():

    global state_communication

    if (state_communication == False):       
        if not os.path.exists(Config.SAVE_REPORT_FOLDER):            
            os.makedirs(Config.SAVE_REPORT_FOLDER)
        if not os.path.exists(Config.SAVE_REPORT_FOLDER + '/'+ str(Config.NAME_SAVE_FOLDER)):
            os.makedirs(Config.SAVE_REPORT_FOLDER + '/'+ str(Config.NAME_SAVE_FOLDER))
        
        print("file     " + Config.figure.file)
        print("SAVE_REPORT_FOLDER   " + Config.SAVE_REPORT_FOLDER)
        print("NAME_SAVE_FOLDER     " + Config.NAME_SAVE_FOLDER)
        shutil.copy(Config.figure.file,Config.SAVE_REPORT_FOLDER + '/'+ str(Config.NAME_SAVE_FOLDER) + '/' )
        
        Config.figure.saveFig(Config.SAVE_REPORT_FOLDER,Config.NAME_SAVE_FOLDER,Config.NAME_SAVE_FIGURE)
        Windows.messageShowinfo("Report generation","Report generation successfully created.")

    else :
        Windows.messageShowwarning("Report generation warning","Warning : please stop the data receive before to generate the report.")


def state_set_communication(start_button,stop_button,state):

    global state_communication
    #if the user click on the start button
    if(state==True):
        logging.info(currentTime() + ' start decoding')
        state_communication=True
        #Config.TIME_FOLDER = str(time.strftime('%Y_' '%m_' '%d_''%H_' '%M_' '%S'))
        
        #disable start button
        start_button.disable()

        #enable stop button
        stop_button.enable()  
        

    elif(state==False):
        if (Windows.messageAskyesno("End of data receive", "Do you want to stop the data receive ?")):
            logging.warning(currentTime() + ' stop decoding')
            state_communication=False

            #enable start button
            start_button.enable()

            #disable stop button
            stop_button.disable()



def add_sensor_save_Function(add_sensor_interface,sensor_add_name):
    
    save_condition = True

    if(sensor_add_name.getEntry()==""):
        logging.warning(currentTime()+ ' add new sensor : no name given')
        Windows.messageShowerror("Name error","Please enter the sensor's name")
        save_condition=False

    #check that the sensor does not already exist
    if(os.path.isfile(sensor_add_name.getEntry().lower() + ".hpp") or os.path.isfile(sensor_add_name.getEntry().lower() + ".cpp")):
        logging.warning(currentTime() + ' sensor name ' + sensor_add_name.getEntry().lower() +' already exit')
        Windows.messageShowerror("Name error",sensor_add_name.getEntry().lower() + " sensor already exist. Please change the sensor's name")
        save_condition=False
    
    
    #if no error, create the hpp and the cpp
    
    if(save_condition==True):
        # Creation of sensor.hpp
        hpp = open(sensor_add_name.getEntry().lower() + ".hpp", "x")
            
        hpp.write("#ifndef DOLMEN_"+ sensor_add_name.getEntry().upper() +"_HPP")
        hpp.write("\n#define DOLMEN_" + sensor_add_name.getEntry().upper() +"_HPP 1")
        hpp.write("\n#include <string>")
        hpp.write("""\nnamespace dolmen
{
""")
        hpp.write("\n   class " + sensor_add_name.getEntry().capitalize())
        hpp.write(""": public Sensor \n  {
    public : """)                   
        hpp.write(sensor_add_name.getEntry().capitalize() + " (int id, std::string name);")
        hpp.write("""
            
    void decoding(const std::string data) override;

    std::string getColumnIdentifiers() override
    {
    """)
        hpp.write("      return "  + '"' + sensor_add_name.getEntry().capitalize() + '";')
        hpp.write("""
    }""")
        hpp.write("""
                
    int getNbAttr() override
    {
      return 1;
    }
  };
}

#endif""")
            
        hpp.close()
        
        # Creation of sensor.cpp
        cpp = open(sensor_add_name.getEntry().lower() + ".cpp", "x")
        cpp.write('#include "' + sensor_add_name.getEntry().lower() + '.hpp"')
        cpp.write("""
            
namespace dolmen
{
""")
        cpp.write("  " + sensor_add_name.getEntry().capitalize() + "::" + sensor_add_name.getEntry().capitalize() + " (int id, std::string name):Sensor{id,name}{}")
        cpp.write("""
            
  void """ + sensor_add_name.getEntry().capitalize() +"""::decoding(const std::string data)
  {
    //insert here the decoding method of your sensor
  }
} /* dolmen */""")
        cpp.close()
        logging.info(currentTime() + ' sensor ' + str(sensor_add_name.getEntry()).lower() +" generated")
        Windows.messageShowinfo("Sensor generation",sensor_add_name.getEntry().lower() + " sensor generation successfully created. Do not forget to complete the decoding function of this class")
        Config.sensors_management_Function(add_sensor_interface)


