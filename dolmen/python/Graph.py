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

    def __init__(self,x,y,row,cols,width,height):

        self.figure = plt.figure(figsize=(x,y),constrained_layout=False)
        #Create figure grid
        self.grid= self.figure.add_gridspec(nrows=row, ncols=cols, width_ratios = width, height_ratios = height)


    def addToWindows(self,windows):

        self.windows = windows
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.windows)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # add matplot tools
        toolbar = NavigationToolbar2Tk( self.canvas, self.windows)
        toolbar.update()
        self.canvas._tkcanvas.pack(side="top", fill="both", expand=1)        
        self.figure._toolbar = toolbar


class GraphPlot():

    def __init__(self,fig,position,title,titleX,titleY,color,label,ylim,x,y):

        self.figure = fig.figure.add_subplot(position)
        plt.tight_layout()
        self.color = color 
        self.title=title
        self.titleX=titleX
        self.titleY=titleY
        self.ylim=ylim
        self.x=x
        self.y=y
        self.label=label
        self.index = count()
        self.figure.set_title(self.title,loc='right') 
        self.figure.set_xlabel(self.titleX)
        self.figure.set_ylabel(self.titleY)
        self.figure.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
        self.figure.set_ylim(self.ylim)


    def animate(self):
        
        self.x.append(next(self.index))     
        self.figure.cla() # Clear the current axes
        
        for i in range(0,len(self.y)):
            value=random.randint(0, 5)
            self.y[i].append(value)
            self.figure.set_title(self.title,loc='right') 
            self.figure.set_xlabel(self.titleX)
            self.figure.set_ylabel(self.titleY)
            self.figure.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
            self.figure.set_ylim(self.ylim)
            self.figure.plot(self.x, self.y[i],color = self.color[i],label =str(self.label[i]) + " = " + str(value))
            self.figure.legend(loc="lower left")
            

class Graph3d():

    def __init__(self,fig,position,title,titleX,titleY,titleZ,marker,color,xlim,ylim,zlim,x,y,z):

        self.figure = fig.figure.add_subplot(position,projection='3d')
        plt.tight_layout()
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

    
    def animate(self):

        value=random.randint(-10, 10)
        value2=random.randint(-10, 10)
        value3=random.randint(-10, 10)
        self.x.append(value)
        self.y.append(value2)
        self.z.append(value3) 
        self.figure.cla() # Clear the current axes
        self.figure.scatter(value,value2,value3,c=self.color,label =
"""x = """ + str(value) + "  " + 
        """
y = """ + str(value2) + "  " +
        """
z = """ + str(value3) + "  ",linestyle='--', marker=self.marker)
        self.figure.plot3D([value, 0], [value2, 0], [value3, 0],self.color)
        self.figure.legend(loc="best")
        self.figure.set_title(self.title,loc='right') 
        self.figure.set_xlabel(self.titleX)
        self.figure.set_ylabel(self.titleY)
        self.figure.set_zlabel(self.titleZ)
        self.figure.set_xlim3d(self.xlim3D)
        self.figure.set_ylim3d(self.ylim3D)
        self.figure.set_zlim3d(self.zlim3D)

class Graph3dGPS():

    def __init__(self,fig,position,title,titleX,titleY,titleZ,marker,color,xlim,ylim,zlim,x,y,z):

        self.figure = fig.figure.add_subplot(position,projection='3d')
        plt.tight_layout()
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