import Windows
import Widgets
import Graph
import os.path
import Config
import csv
import time

#My figure creation
figure=Graph.Graph(20,8,3,3,[4,4,4],[4,2,2])
myFigure = figure.figure
f1= Graph.GraphPlot(figure,figure.grid[1, 0:3],"Temperator","time","Temperator",["blue","red"],["Sensor 1","Sensor 2"],[-45, 45],2)
f2= Graph.GraphPlot(figure,figure.grid[2, 0:3],"Pression","time","Pression",["red","green"],["Sensor 1","Sensor 2"],[-50, 50],2)
f3= Graph.Graph3d(figure,figure.grid[0, 0],"Acceleration","x acceleration","y acceleration","z acceleration",'o','red',(-10,10),(-10,10),(-10,10),[],[],[],False)
f4= Graph.Graph3d(figure,figure.grid[0, 1],"Gyroscope","x gyroscope","y gyroscope","z gyroscope",'o','black',(-10,10),(-10,10),(-10,10),[],[],[],False)
#f5= Graph.Graph3dGPS(figure,figure.grid[0, 2],"GPS","x","y","z",'o','black',(-1000,1000),(-1000,1000),(-1000,1000),[],[],[])
f5= Graph.Graph3d(figure,figure.grid[0, 2],"GPS","x","y","z",'o','black',(-1000,1000),(-1000,1000),(-1000,1000),[],[],[],True)
myGraph=[f1,f2,f3,f4,f5]

sensors = [["temp1",False],["temp2",False],["pressure1",False],["pressure2",False],["acc",False],["gyro",False]]

count=0 # current line in CSV
state_communication=False

def decodingCSV():

    global count, state_communication,sensors
   
    filename = open(figure.file, 'r', encoding='latin1')
          
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

    # line split processing
    for j in range(0,len(line_split)):
    
        if line_split[j]=='time': #time decoding and processing

            x=float(line_split[j+2])
            f1.x.append(x)
            f2.x.append(x) 
             
        if line_split[j]=='temp1': #if sensor is detected

            sensors[0][1] = True # sensors data is processed
            if str(line_split[j+2]) !="": # if there are sensors's data
                f1.y[0].append(float(line_split[j+2])) # adding sensors's data in graph

            else : # if there are not sensors's data
                f1.y[0].append(0) # adding 0 in graph           
            
                    
        if line_split[j]=='temp2': #if sensor is detected

            sensors[1][1] = True # sensors data is processed
            if str(line_split[j+2])!="": # if there are sensors's data
                f1.y[1].append(float(line_split[j+2])) # adding sensors's data in graph

            else : # if there are not sensors's data
                f1.y[1].append(0) # adding 0 in graph    
                 
        
        if line_split[j]=='pressure1': #if sensor is detected

            sensors[2][1] = True # sensors data is processed
            if str(line_split[j+2])!="": # if there are sensors's data
                f2.y[0].append(float(line_split[j+2])) # adding sensors's data in graph

            else : # if there are not sensors's data
                f2.y[0].append(0) # adding 0 in graph    
            
                
        if line_split[j]=='pressure2': #if sensor is detected

            sensors[3][1] = True # sensors data is processed
            if str(line_split[j+2])!="": # if there are sensors's data
                f2.y[1].append(float(line_split[j+2])) # adding sensors's data in graph

            else : # if there are not sensors's data
                f2.y[1].append(0) # adding 0 in graph    
            
                   
        if line_split[j]=='acc': #if sensor is detected

            sensors[4][1] = True # sensors data is processed
            if str(line_split[j+2])!="" and str(line_split[j+3])!="" and str(line_split[j+4])!="": # if x, y, z sensors's data are not empty
                # adding sensors's data in graph
                f3.x.append(float(line_split[j+2]))
                f3.y.append(float(line_split[j+3]))
                f3.z.append(float(line_split[j+4]))

            else: # if x or y or z sensors's data are empty
                # adding 0 in graph   
                f3.x.append(0)
                f3.y.append(0)
                f3.z.append(0)

        if line_split[j]=='gyro': #if sensor is detected

            sensors[5][1] = True # sensors data is processed
            if str(line_split[j+2])!="" and str(line_split[j+3])!="" and str(line_split[j+4])!="": # if x, y, z sensors's data are not empty
                # adding sensors's data in graph
                f4.x.append(float(line_split[j+2]))
                f4.y.append(float(line_split[j+3]))
                f4.z.append(float(line_split[j+4]))

            else: # if x or y or z sensors's data are empty
                # adding 0 in graph   
                f4.x.append(0)
                f4.y.append(0)
                f4.z.append(0)

    # Verifing if sensors was processed
    for i in range(0,len(sensors)):

        # If sensors was not processed
        if sensors[i][1]==False :

            if sensors[i][0]=='temp1':
                f1.y[0].append(0)
                print("no sensors temp1")

            if sensors[i][0]=='temp2':
                f1.y[1].append(0)
                print("no sensors temp2")

            if sensors[i][0]=='pressure1':
                f2.y[0].append(0)
                print("no sensors pressure1")

            if sensors[i][0]=='pressure2':
                f2.y[1].append(0)
                print("no sensors pressure2") 

            if sensors[i][0]=='acc':
                f3.x.append(0)
                f3.y.append(0)
                f3.z.append(0)
                print("no sensors acc")  
                
            if sensors[i][0]=='gyro':
                f4.x.append(0)
                f4.y.append(0)
                f4.z.append(0)
                print("no sensors gyro")      
        
        else: # Reseting if sensors was processed
            sensors[i].pop() 
            sensors[i].append(False)
    #update line        
    count+=1

    filename.close()

def fileExist(start_button,stop_button,figure):

    try:
        with open(figure.file,'r',encoding='latin1') as filename:
            return  True

    except:     
        condition =  False
        Windows.messageShowwarning("Open Filename", "Warning, Problem detected with CSV file ")

        return False


def updateOffline(i):

    global myGraph,state_communication,figure

    if(state_communication==True and fileExist(start_button,stop_button,figure)==True): #if you click on the start button of fire_interface windows and csv name exist
        decodingCSV() # decoding csv
        if(state_communication==True): 
            for graph in myGraph:               
                graph.animate() # update graph


def updateOnline(i,start_button,stop_button):
    global myGraph,state_communication,figure

    if(state_communication==True and fileExist(start_button,stop_button,figure)==True): #if you click on the start button of fire_interface windows and csv name exist
        decodingCSV() # decoding csv
        if(state_communication==True): 
            for graph in myGraph:               
                graph.animate() # update graph
            
def report_Function():

    global myfigure,state_communication

    if (state_communication == False):
        myFigure.savefig('reportTest.png')
        Windows.messageShowinfo("Report generation","Report generation successfully created.")

    else :
        Windows.messageShowwarning("Report generation warning","Warning : please stop the data receive before to generate the report.")


def state_set_communication(start_button,stop_button,state):

    global state_communication
    #if the user click on the start button
    if(state==True):
        state_communication=True

        #disable start button
        start_button.disable()

        #enable stop button
        stop_button.enable()  
        

    elif(state==False):
        if (Windows.messageAskyesno("End of data receive", "Do you want to stop the data receive ?")):
            state_communication=False

            #enable start button
            start_button.enable()

            #disable stop button
            stop_button.disable()



def add_sensor_save_Function(add_sensor_interface,sensor_add_name, sensor_add_arg1,sensor_add_arg1_type,sensor_add_arg2,sensor_add_arg2_type,sensor_add_arg3,sensor_add_arg3_type,sensor_add_arg4,sensor_add_arg4_type):
    
    save_condition = True

    if(sensor_add_name.getEntry()==""):
        Windows.messageShowerror("Name error","Please enter the sensor's name")
        save_condition=False

    #check that the sensor does not already exist
    if(os.path.isfile(sensor_add_name.getEntry() + ".hpp")):
        Windows.messageShowerror("Name error",sensor_add_name.getEntry() + " sensor already exist. Please change the sensor's name")
        save_condition=False

    #check that for the given arguments their type is given
    if(len(sensor_add_arg1.getEntry())!=0 and len(sensor_add_arg1_type.getEntry())==0 or
       len(sensor_add_arg2.getEntry())!=0 and len(sensor_add_arg2_type.getEntry())==0 or
       len(sensor_add_arg3.getEntry())!=0 and len(sensor_add_arg3_type.getEntry())==0 or
       len(sensor_add_arg4.getEntry())!=0 and len(sensor_add_arg4_type.getEntry())==0):
        save_condition=False
        Windows.messageShowerror("Argument error","Please enter the type of argument given ")

    #check that for the given arguments their name is given
    if(len(sensor_add_arg1.getEntry())==0 and len(sensor_add_arg1_type.getEntry())!=0 or
       len(sensor_add_arg2.getEntry())==0 and len(sensor_add_arg2_type.getEntry())!=0 or
       len(sensor_add_arg3.getEntry())==0 and len(sensor_add_arg3_type.getEntry())!=0 or
       len(sensor_add_arg4.getEntry())==0 and len(sensor_add_arg4_type.getEntry())!=0):
        save_condition=False
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
            Windows.messageShowinfo("Sensor generation",sensor_add_name.getEntry() + " sensor generation successfully created. Do not forget to complete the decoding function of this class")
            Config.sensors_management_Function(add_sensor_interface)


