import matplotlib
matplotlib.use('TkAgg')
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
#import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import tkinter as tk
from itertools import count
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm
import matplotlib.markers as marker


class Graph():

    def __init__(self,x,y,row,column,width,height):
        self.x=x
        self.y=y
        self.row=row
        self.column = column 
        self.width=width
        self.height=height
        self.figure = plt.figure(figsize=(self.x,self.y),constrained_layout=False)
        
        #Create figure grid
        self.grid= self.figure.add_gridspec(nrows=self.row, ncols=self.column, width_ratios = self.width, height_ratios = self.height,wspace = 0.2,hspace=0.5)
        self.file = None

    def addToWindows(self,windows,rowGraph,columnGraph,columnspan,rowToolbar,columnToolbar):
        self.windows = windows
        self.rowGraph=rowGraph
        self.columnGraph=columnGraph
        self.columnspan=columnspan
        self.rowToolbar=rowToolbar
        self.columnToolbar=columnToolbar
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.windows)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas._tkcanvas.grid(row=self.rowGraph, column=self.columnGraph,columnspan=self.columnspan,ipadx=1,ipady=1,padx=1,pady=1,sticky="w")
        
        # add matplot tools
        self.toolbarFrame = tk.Frame(self.windows)
        self.toolbarFrame.grid(row=self.rowToolbar,column=self.columnToolbar)
        toolbar = NavigationToolbar2Tk( self.canvas, self.toolbarFrame)
        toolbar.update()
        
    
    def saveFig(self,SAVE_REPORT_FOLDER,NAME_SAVE_FOLDER,NAME_SAVE_FIGURE):
        self.figure.savefig(SAVE_REPORT_FOLDER + '/' + NAME_SAVE_FOLDER + '/' + NAME_SAVE_FIGURE)
        

class GraphPlot():

    def __init__(self,fig,position,title,titleX,titleY,color,label,ylim,numberGraph):

        self.figure = fig.figure.add_subplot(position)
        self.color = color 
        self.title=title
        self.titleX=titleX
        self.titleY=titleY
        self.ylim=ylim
        self.x=[]
        self.y=[]
        self.numberGraph=numberGraph
        for i in range(0,self.numberGraph):
            self.y.append([])
        self.label=label
        self.index = count()
        self.figure.set_title(self.title,loc='right') 
        self.figure.set_xlabel(self.titleX)
        self.figure.set_ylabel(self.titleY)
        self.figure.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
        self.figure.set_ylim(self.ylim)
        self.figure.format_coord = lambda x, y: ''

    def animate(self):        
                  
        self.figure.cla() # Clear the current axes
        
        for i in range(0,len(self.y)):
            self.figure.set_title(self.title,loc='right') 
            self.figure.set_xlabel(self.titleX)
            self.figure.set_ylabel(self.titleY)
            self.figure.set_ylim(self.ylim)
            self.figure.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)

            if len(self.label) == self.numberGraph:           
                self.figure.plot(self.x, self.y[i],color = self.color[i],label =str(self.label[i] + " = " + str(self.y[i][-1])))
                self.figure.legend(loc="lower left")
            else :
                self.figure.plot(self.x, self.y[i],color = self.color[i])
                
    def reset(self):
        self.figure.cla()
        self.x=[]
        self.y=[]
        for i in range(0,self.numberGraph):
            self.y.append([])
            
class Graph3d():

    def __init__(self,fig,position,title,titleX,titleY,titleZ,marker,color,xlim,ylim,zlim,typeGraph):

        self.figure = fig.figure.add_subplot(position,projection='3d')
        self.x=[]
        self.y=[]
        self.z=[]        
        self.title=title
        self.titleX=titleX
        self.titleY=titleY
        self.titleZ=titleZ
        self.marker=marker
        self.color =color
        self.xlim3D = xlim
        self.ylim3D = ylim
        self.zlim3D = zlim
        self.index = count()
        self.figure.set_title(self.title,loc='right') 
        self.figure.set_xlabel(self.titleX)
        self.figure.set_ylabel(self.titleY)
        self.figure.set_zlabel(self.titleZ)
        self.figure.set_xlim3d(self.xlim3D)
        self.figure.set_ylim3d(self.ylim3D)
        self.figure.set_zlim3d(self.zlim3D)
        self.figure.view_init(azim=-60)
        self.figure.format_coord = lambda x, y: ''
        self.typeGraph=typeGraph
        #self.index = count()
    
    def animate(self):   
           
        self.figure.cla() # Clear the current axes
        self.figure.set_xlabel(self.titleX)
        self.figure.set_ylabel(self.titleY)
        self.figure.set_zlabel(self.titleZ)
        self.figure.set_xlim3d(self.xlim3D)
        self.figure.set_ylim3d(self.ylim3D)
        self.figure.set_zlim3d(self.zlim3D)
        self.figure.set_title(self.title,loc='right')

        if(self.typeGraph==False):

            
            #self.figure.scatter(self.x[-1],self.y[-1],self.z[-1],c=self.color,linestyle='--', marker=self.marker)
            self.figure.scatter(self.x[-1],self.y[-1],self.z[-1],c=self.color,label =
    """  
    """ + str(self.titleX) + " = " + str(self.x[-1]) + """  
    """ + 
            
    str(self.titleY) + " = " + str(self.y[-1]) + """  
    """ +
            
    str(self.titleZ) + " = " + str(self.z[-1]) + """  
    """,linestyle='--', marker=self.marker)
            self.figure.plot3D([self.x[-1], 0], [self.y[-1], 0], [self.z[-1], 0],self.color)

            self.figure.legend(loc="best")             
        
        else:

            self.x.append(-next(self.index))
            self.y.append(next(self.index))
            self.z.append(next(self.index)) 
            self.figure.scatter(self.x,self.y,self.z,c=self.color,label =
    """  
    """ + str(self.titleX) + " = " + str(self.x[-1]) + """  
    """ + 
            
    str(self.titleY) + " = " + str(self.y[-1]) + """  
    """ +
            
    str(self.titleZ) + " = " + str(self.z[-1]) + """  
    """,linestyle='--', marker=self.marker)

            self.figure.legend(loc="best")
    def reset(self):
        self.figure.cla()
        self.x=[]
        self.y=[]
        self.z=[]
            
"""        
class Graph3dGPS():

    def __init__(self,fig,position,title,titleX,titleY,titleZ,marker,color,xlim,ylim,zlim,x,y,z):

        self.figure = fig.figure.add_subplot(position,projection='3d')
        #plt.tight_layout()
        self.x=x
        self.y=y
        self.z=z       
        self.title=title
        self.titleX=titleX
        self.titleY=titleY
        self.titleZ=titleZ
        self.marker=marker
        self.color =color
        self.xlim3D = xlim
        self.ylim3D = ylim
        self.zlim3D = zlim
        self.index = count()
        self.figure.set_title(self.title,loc='right') 
        self.figure.set_xlabel(self.titleX)
        self.figure.set_ylabel(self.titleY)
        self.figure.set_zlabel(self.titleZ)
        self.figure.set_xlim3d(self.xlim3D)
        self.figure.set_ylim3d(self.ylim3D)
        self.figure.set_zlim3d(self.zlim3D)
        self.figure.format_coord = lambda x, y: ''
        
    
    def animate(self):

        
        self.x.append(-next(self.index))
        self.y.append(next(self.index))
        self.z.append(next(self.index)) 
        self.figure.cla() # Clear the current axes
        self.figure.scatter(self.x,self.y,self.z,c=self.color,linestyle='--', marker=self.marker)
        self.figure.set_title(self.title,loc='right') 
        self.figure.set_xlabel(self.titleX)
        self.figure.set_ylabel(self.titleY)
        self.figure.set_zlabel(self.titleZ)
        self.figure.set_xlim3d(self.xlim3D)
        self.figure.set_ylim3d(self.ylim3D)
        self.figure.set_zlim3d(self.zlim3D)
"""
