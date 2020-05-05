import Windows
import Widgets
import Graph
import os.path
import Config


#My figure creation
figure=Graph.Graph(10,8,3,3,[4, 4, 4],[6,3,3])
myFigure = figure.figure
#gs = myFigure.add_gridspec(3, 3, width_ratios = [4, 4, 4], height_ratios = [6,3,3])
f1= Graph.GraphPlot(figure,figure.grid[1, 0:3],"Temperator","time","Temperator",["blue","red"],["Sensor 1","Sensor 2"],[0, 8],[],[[],[]])
f2= Graph.GraphPlot(figure,figure.grid[2, 0:3],"Pression","time","Pression",["red","green"],["Sensor 1","Sensor 2"],[0, 10],[],[[],[]])
f3= Graph.Graph3d(figure,figure.grid[0, 0],"Acceleration","x acceleration","y acceleration","z acceleration",'o','red',(-10,10),(-10,10),(-10,10),[],[],[])
f4= Graph.Graph3d(figure,figure.grid[0, 1],"Gyroscope","x gyroscope","y gyroscope","z gyroscope",'o','black',(-10,10),(-10,10),(-10,10),[],[],[])
f5= Graph.Graph3dGPS(figure,figure.grid[0, 2],"GPS","x","y","z",'o','black',(-1000,1000),(-1000,1000),(-1000,1000),[],[],[])
myGraph=[f1,f2,f3,f4,f5]

state_communication=False


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


def update(i):

    global timer,myGraph,state_communication

    if(state_communication==True): #if you click on the start button of fire_interface windows => update graph
        for graph in myGraph :       
            graph.animate()      
            timer.update_clock()
    

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

