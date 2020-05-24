import Dolmen
import Graph
import time
import logging
class Sensors():

    def __init__(self,name,idSensor,idGraph,typeGraph,graph):
        self.name=name
        self.idSensor=idSensor
        self.idGraph=idGraph
        self.processed=False
        self.typeGraph=typeGraph
        self.graph=graph
        
        
    def decoding(self,line_split):
        
        for j in range(0,len(line_split)):                 
            if self.typeGraph ==False : # if graph 2D
                if line_split[j]==str(self.idSensor) and line_split[j+1]==self.name: #if sensor is detected
                    self.processed = True # sensors data is processed
                    if str(line_split[j+2]) !="": # if there are sensors's data
                        self.graph.y[self.idGraph].append(float(line_split[j+2])) # adding sensors's data in graph

                    else : # if there are not sensors's data
                        logging.warning(Dolmen.currentTime() + ' no data in sensors ' + str(self.name) + str(self.idSensor))
                        self.graph.y[self.idGraph].append(0) # adding 0 in graph
                        print(' no data in sensors ' + str(self.name) + " " + str(self.idSensor))
                        
            elif self.typeGraph ==True : # if graph 3D
                if line_split[j]==str(self.idSensor) and line_split[j+1]==self.name[0] and line_split[j+3]==self.name[1] and line_split[j+5]==self.name[2]: #if sensor is detected

                    self.processed = True # sensors data is processed
                    if str(line_split[j+2])!="" and str(line_split[j+4])!="" and str(line_split[j+6])!="": # if x, y, z sensors's data are not empty
                        # adding sensors's data in graph
                        self.graph.x.append(float(line_split[j+2]))
                        self.graph.y.append(float(line_split[j+4]))
                        self.graph.z.append(float(line_split[j+6]))

                    else: # if x or y or z sensors's data are empty
                        # adding 0 in graph  
                        logging.warning(Dolmen.currentTime() + ' no data in sensors ' + str(self.name) + " " + str(self.idSensor))
                        self.graph.x.append(0)
                        self.graph.y.append(0)
                        self.graph.z.append(0)
                        print(' no data in sensors ' + str(self.name) + " " + str(self.idSensor))
    def verifing(self):
        if self.processed==False :
            if self.typeGraph ==False : # if graph 2D:
                self.graph.y[self.idGraph].append(0)
                print("no sensors " + str(self.name) + " " + str(self.idSensor))
                logging.warning(Dolmen.currentTime() + ' no sensors ' + str(self.name) + " " + str(self.idSensor))
                
            elif self.typeGraph ==True : # if graph 3D
                logging.warning(Dolmen.currentTime() + ' no sensors ' + str(self.name) + " " + str(self.idSensor))
                print("no sensors " + str(self.name) + " " + str(self.idSensor))
                self.graph.x.append(0)
                self.graph.y.append(0)
                self.graph.z.append(0)
        
        else: # Reseting if sensors was processed
            self.processed =False
