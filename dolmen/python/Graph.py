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

    def __init__(self,x,y,row,column,width,height,colorText,xColor,yColor,axeLabelColor,gridColor,colorFont):
        self.x=x
        self.y=y
        self.row=row
        self.column = column 
        self.width=width
        self.height=height
        self.colorFont=colorFont
        self.colorText=colorText
        self.xColor=xColor
        self.yColor=yColor
        self.axeLabelColor=axeLabelColor
        self.gridColor=gridColor
        self.figure = plt.figure(figsize=(self.x,self.y),constrained_layout=False,facecolor=self.colorFont)
        matplotlib.rcParams['text.color'] = self.colorText
        matplotlib.rcParams['xtick.color'] = self.xColor
        matplotlib.rcParams['ytick.color'] = self.yColor
        matplotlib.rcParams['axes.labelcolor'] = self.axeLabelColor
        matplotlib.rcParams['grid.color'] = self.gridColor
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

    def __init__(self,fig,position,title,titleX,titleY,ylim,facecolor,graphLegend,ySide):
        self.fig=fig
        self.facecolor=facecolor
        self.figure = self.fig.figure.add_subplot(position,facecolor=self.facecolor)
        self.color = [] 
        self.graphLegend=graphLegend
        self.title=title
        self.titleX=titleX
        self.titleY=titleY
        self.ylim=ylim
        self.x=[]
        self.y=[]
        self.numberGraph=0        
        self.label=[]
        if ySide=="right":
            self.figure.yaxis.set_label_position("right")
            self.figure.yaxis.tick_right()
        if ySide=="left":
            self.figure.yaxis.set_label_position("left")
            self.figure.yaxis.tick_left()

        self.figure.set_title(self.title,loc='right') 
        self.figure.set_xlabel(self.titleX)
        self.figure.set_ylabel(self.titleY)
        self.figure.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
        self.figure.set_ylim(self.ylim)
        self.figure.format_coord = lambda x, y: ''

    def animate(self):        
        self.figure.cla() # Clear the current axes
        self.figure.set_title(self.title,loc='right') 
        self.figure.set_xlabel(self.titleX)
        self.figure.set_ylabel(self.titleY)
        self.figure.set_ylim(self.ylim)
        for i in range(0,len(self.y)):
            
            self.figure.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)

            if len(self.label) == self.numberGraph: 
                self.figure.plot(self.x, self.y[i],color = self.color[i],label =str(self.label[i] + " = " + str(self.y[i][-1])))
                self.figure.legend(facecolor=self.graphLegend,loc="lower left")
            else :
                self.figure.plot(self.x, self.y[i],color = self.color[i])
                
    def initGraph(self):
        self.figure.cla()
        self.x=[]
        self.y=[]
        for i in range(0,self.numberGraph):
            self.y.append([])
            
class Graph3d():

    def __init__(self,fig,position,title,titleX,titleY,titleZ,xlim,ylim,zlim,typeGraph,facecolor,graphLegend):
        self.facecolor=facecolor
        self.figure = fig.figure.add_subplot(position,projection='3d',facecolor=self.facecolor)
        self.x=[]
        self.y=[]
        self.z=[]
        self.facecolor=facecolor        
        self.title=title
        self.titleX=titleX
        self.titleY=titleY
        self.titleZ=titleZ
        self.marker=None
        self.color =None
        self.graphLegend=graphLegend
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

            if self.titleX != "" and self.titleY != "" and self.titleZ != "":
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
                self.figure.plot3D([self.x[-1], 0], [self.y[-1], 0], [self.z[-1], 0],self.color)
                self.figure.legend(facecolor=self.graphLegend,loc="best")             
            else:
                #self.figure.scatter(self.x[-1],self.y[-1],self.z[-1],c=self.color,linestyle='--', marker=self.marker)
                self.figure.scatter(self.x[-1],self.y[-1],self.z[-1],c=self.color,linestyle='--', marker=self.marker)
                self.figure.plot3D([self.x[-1], 0], [self.y[-1], 0], [self.z[-1], 0],self.color)

                
        else:

            self.x.append(-next(self.index))
            self.y.append(next(self.index))
            self.z.append(next(self.index)) 
            if self.titleX != "" and self.titleY != "" and self.titleZ != "":
                self.figure.scatter(self.x,self.y,self.z,c=self.color,label =
        """  
        """ + str(self.titleX) + " = " + str(self.x[-1]) + """  
        """ + 
                
        str(self.titleY) + " = " + str(self.y[-1]) + """  
        """ +
                
        str(self.titleZ) + " = " + str(self.z[-1]) + """  
        """,linestyle='--', marker=self.marker)

                self.figure.legend(facecolor=self.graphLegend,loc="best")
            else:
                self.figure.scatter(self.x,self.y,self.z,c=self.color,linestyle='--', marker=self.marker)
    def initGraph(self):
        self.figure.cla()
        self.x=[]
        self.y=[]
        self.z=[]

class GraphHist():
    def __init__(self,fig,position,title,titleX,titleY,ylim,facecolor,ySide):
        
        self.facecolor=facecolor
        self.figure = fig.figure.add_subplot(position,facecolor=self.facecolor)
        self.color = [] 
        self.title=title
        self.titleX=titleX
        self.titleY=titleY
        self.ylim=ylim
        self.x=[]
        self.y=[]
        self.numberGraph=0
        self.position=None
        if ySide=="right":
            self.figure.yaxis.set_label_position("right")
            self.figure.yaxis.tick_right()
        if ySide=="left":
            self.figure.yaxis.set_label_position("left")
            self.figure.yaxis.tick_left()
        self.figure.set_title(self.title,loc='right') 
        self.figure.set_xlabel(self.titleX)
        self.figure.set_ylabel(self.titleY)
        self.figure.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
        self.figure.set_ylim(self.ylim)
        self.figure.format_coord = lambda x, y: ''
        self.width = 0.35 

    def animate(self):        
                  
        self.figure.cla() # Clear the current axes
        self.figure.set_title(self.title,loc='right') 
        self.figure.set_xlabel(self.titleX)
        self.figure.set_ylabel(self.titleY)
        #self.figure.set_ylim(self.ylim)
        self.position=np.arange(self.numberGraph)
        self.figure.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
        print(self.y)
        self.figure.bar(self.position, np.array(self.y), color=self.color, edgecolor='black')
        self.figure.set_xticks(self.position)
        self.figure.set_xticklabels(self.x) 

    def initGraph(self):
        self.figure.cla()
        self.y=[]
        for i in range(0,self.numberGraph):
            self.y.append([])

