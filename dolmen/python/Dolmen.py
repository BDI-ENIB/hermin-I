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
    line_split = []
    
    if count+1>len(lines):
        state_communication=False
        print("OH SHIT !!!")
        return       

    for i in lines[count]:
        line_split=i.split(",")
        
    for j in range(0,len(line_split)):
    
        if line_split[j]=='time': #time decoding and processing
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
        sensor.graph.reset()
                
def report_Function():

    global state_communication

    if (state_communication == False):       
        if not os.path.exists(Config.SAVE_REPORT_FOLDER):            
            os.makedirs(Config.SAVE_REPORT_FOLDER)
        if not os.path.exists(Config.SAVE_REPORT_FOLDER + '/'+ str(Config.NAME_SAVE_FOLDER)):
            os.makedirs(Config.SAVE_REPORT_FOLDER + '/'+ str(Config.NAME_SAVE_FOLDER))
        
        shutil.copy(Config.figure.file,Config.SAVE_REPORT_FOLDER + '/'+ str(Config.NAME_SAVE_FOLDER) + '/' +  Config.figure.file)
        #Config.myFigure.savefig('reportTest.png')
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



def add_sensor_save_Function(add_sensor_interface,sensor_add_name, sensor_add_arg1,sensor_add_arg1_type,sensor_add_arg2,sensor_add_arg2_type,sensor_add_arg3,sensor_add_arg3_type,sensor_add_arg4,sensor_add_arg4_type):
    logging.info(currentTime() + ' entering in add sensor mode')
    save_condition = True

    if(sensor_add_name.getEntry()==""):
        logging.warning(currentTime()+ ' sensor name error')
        Windows.messageShowerror("Name error","Please enter the sensor's name")
        save_condition=False

    #check that the sensor does not already exist
    if(os.path.isfile(sensor_add_name.getEntry() + ".hpp")):
        logging.warning(currentTime() + ' sensor name already exit')
        Windows.messageShowerror("Name error",sensor_add_name.getEntry() + " sensor already exist. Please change the sensor's name")
        save_condition=False
        

    #check that for the given arguments their type is given
    if(len(sensor_add_arg1.getEntry())!=0 and len(sensor_add_arg1_type.getEntry())==0 or
       len(sensor_add_arg2.getEntry())!=0 and len(sensor_add_arg2_type.getEntry())==0 or
       len(sensor_add_arg3.getEntry())!=0 and len(sensor_add_arg3_type.getEntry())==0 or
       len(sensor_add_arg4.getEntry())!=0 and len(sensor_add_arg4_type.getEntry())==0):
        save_condition=False
        logging.warning(currentTime() + ' no sensor argument type given')
        Windows.messageShowerror("Argument error","Please enter the type of argument given ")

    #check that for the given arguments their name is given
    if(len(sensor_add_arg1.getEntry())==0 and len(sensor_add_arg1_type.getEntry())!=0 or
       len(sensor_add_arg2.getEntry())==0 and len(sensor_add_arg2_type.getEntry())!=0 or
       len(sensor_add_arg3.getEntry())==0 and len(sensor_add_arg3_type.getEntry())!=0 or
       len(sensor_add_arg4.getEntry())==0 and len(sensor_add_arg4_type.getEntry())!=0):
        save_condition=False
        logging.warning(currentTime() + ' no sensor argument name given')
        Windows.messageShowerror("Argument error","Please enter the name of argument given ")

    #if no error, create the hpp
    else : 
        if(save_condition==True):
            hpp = open(sensor_add_name.getEntry() + ".hpp", "x")
            #upper
            hpp.write("#ifndef DOLMEN_"+ sensor_add_name.getEntry().upper() +"_HPP")
            hpp.write("\n#define DOLMEN_" + sensor_add_name.getEntry().upper() +"_HPP 1")
            hpp.write("\n#include <string>")
            hpp.write("""\nnamespace dolmen
{
""")
            hpp.write("\n   class " + sensor_add_name.getEntry().capitalize())
            hpp.write("""\n  {
    public :""")
            hpp.write("\n      " + sensor_add_name.getEntry().capitalize() + """ (int id, std::string name)
      {
        int id_=id;
        std::string name_=name;""")
            hpp.write("\n        " + sensor_add_arg1_type.getEntry() + " "  + sensor_add_arg1.getEntry() + "_=" + sensor_add_arg1.getEntry() + ";")
            if (len(sensor_add_arg2.getEntry())!=0 and len(sensor_add_arg2_type.getEntry())!=0 ):
                hpp.write("\n        " + sensor_add_arg2_type.getEntry() + " " + sensor_add_arg2.getEntry() + "_=" + sensor_add_arg2.getEntry() + ";")
            if (len(sensor_add_arg3.getEntry())!=0 and len(sensor_add_arg3_type.getEntry())!=0):
                hpp.write("\n        " + sensor_add_arg3_type.getEntry() + " " + sensor_add_arg3.getEntry() + "_=" + sensor_add_arg3.getEntry() + ";")
            if (len(sensor_add_arg4.getEntry())!=0 and len(sensor_add_arg4_type.getEntry())!=0):
                hpp.write("\n        " + sensor_add_arg4_type.getEntry() + " " + sensor_add_arg4.getEntry() + "_=" + sensor_add_arg3.getEntry() + ";")
            hpp.write("""\n      }

""")
            hpp.write("\n      virtual ~" + sensor_add_name.getEntry().capitalize() + "() ")
            hpp.write("""\n      {
        //
      }

      virtual void decoding(const std::string data) = 0;

      int getID()
      {
        return id_;
      }
""")
            hpp.write("\n      " + sensor_add_arg1_type.getEntry() + " get" + sensor_add_arg1.getEntry().capitalize() +"""()
      {
        return """ + sensor_add_arg1.getEntry() +"""_;
      }""")
            
                       
            if (len(sensor_add_arg2.getEntry())!=0 and len(sensor_add_arg2_type.getEntry())!=0):
                hpp.write("\n      " + sensor_add_arg2_type.getEntry() + " get" + sensor_add_arg2.getEntry().capitalize() +"""()
      {
        return """ + sensor_add_arg2.getEntry() +"""_;
      }""")
            
            if (len(sensor_add_arg3.getEntry())!=0 and len(sensor_add_arg3_type.getEntry())!=0):
                hpp.write("\n      " + sensor_add_arg3_type.getEntry() + " get" + sensor_add_arg3.getEntry().capitalize() +"""()
      {
        return """ + sensor_add_arg3.getEntry() +"""_;
      }""")

            if (len(sensor_add_arg4.getEntry())!=0 and len(sensor_add_arg4_type.getEntry())!=0):
                hpp.write("\n      " + sensor_add_arg4_type.getEntry() + " get" +sensor_add_arg4.getEntry().capitalize() +"""()
      {
        return """ + sensor_add_arg4.getEntry() +"""_;
      }""")
            hpp.write("""\n    private :
      int id_;
      std::string name_""")  
            hpp.write("\n      " + sensor_add_arg1_type.getEntry() + " " + sensor_add_arg1.getEntry() + "_;")
            if (len(sensor_add_arg2.getEntry())!=0 and len(sensor_add_arg2_type.getEntry())!=0):
                hpp.write("\n      " + sensor_add_arg2_type.getEntry() + " " + sensor_add_arg2.getEntry() + "_;")
            if (len(sensor_add_arg3.getEntry())!=0 and len(sensor_add_arg3_type.getEntry())!=0):
                hpp.write("\n      " + sensor_add_arg3_type.getEntry() + " " + sensor_add_arg3.getEntry() + "_;")
            if (len(sensor_add_arg4.getEntry())!=0 and len(sensor_add_arg4_type.getEntry())!=0):
                hpp.write("\n      " + sensor_add_arg4_type.getEntry() + " " + sensor_add_arg4.getEntry() + "_;")
            hpp.write("""\n  };
}

#endif
""")
            hpp.close()
            
            logging.info(currentTime() + ' sensor ' + str(sensor_add_name.getEntry()) +" generated")
            Windows.messageShowinfo("Sensor generation",sensor_add_name.getEntry() + " sensor generation successfully created. Do not forget to complete the decoding function of this class")
            Config.sensors_management_Function(add_sensor_interface)


