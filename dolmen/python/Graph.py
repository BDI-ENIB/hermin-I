import matplotlib
matplotlib.use('TkAgg')
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
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
        #initialise figure parameters
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
    
    def saveFig(self,SAVE_REPORT_FOLDER,NAME_SAVE_FOLDER,NAME_SAVE_FIGURE):# save figure
        self.figure.savefig(SAVE_REPORT_FOLDER + '/' + NAME_SAVE_FOLDER + '/' + NAME_SAVE_FIGURE)
        

class GraphPlot(): # 2D Graphe

    def __init__(self,fig,position,title,titleX,titleY,xlim,ylim,facecolor,graphLegend,ySide,typeGraph):
        self.fig=fig
        self.facecolor=facecolor
        self.figure = self.fig.figure.add_subplot(position,facecolor=self.facecolor)
        self.color = [] 
        self.graphLegend=graphLegend
        self.title=title
        self.titleX=titleX
        self.titleY=titleY
        self.xlim=xlim
        self.ylim=ylim
        self.x=[]
        self.y=[]
        self.typeGraph=typeGraph # False x axe = time and True = x axe is like y axe
        self.numberGraph=0        
        self.label=[]
        self.ySide=ySide
        self.figure.format_coord = lambda x, y: ''

    def animate(self):  

        self.figure.cla() # Clear the current axes
        # set figure display parameters
        self.figure.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
        self.figure.set_title(self.title,loc='right') 
        self.figure.set_xlabel(self.titleX)
        self.figure.set_ylabel(self.titleY)
        # set axe limits
        self.figure.set_ylim(self.ylim)
        if len(self.xlim)==2:
            self.figure.set_xlim(self.xlim)
        #update graph
        # if x axe is time
        if self.typeGraph==False:
            for i in range(0,self.numberGraph):
                if len(self.label) == self.numberGraph: # if label to display
                    self.figure.plot(self.x, self.y[i],color = self.color[i],label =str(self.label[i]), marker='o') # + " = " + str(self.y[i][-1])
                    self.figure.legend(facecolor=self.graphLegend,loc="upper left")
                else :
                    self.figure.plot(self.x, self.y[i],color = self.color[i], marker='o')
        # if x axe is like y axe
        if self.typeGraph==True:
            for i in range(0,self.numberGraph):
                if len(self.label) == self.numberGraph: # if no label to display
                    self.figure.plot(self.x[i], self.y[i],color = self.color[i],label =str(self.label[i]), marker='o') # + " = " + str(self.y[i][-1])
                    self.figure.legend(facecolor=self.graphLegend,loc="upper left")
                else :
                    self.figure.plot(self.x[i], self.y[i],color = self.color[i], marker='o')
                                        
    def initGraph(self):

        self.figure.cla()
        self.x=[]
        self.y=[]

        if self.typeGraph==False: # if x axe is time
            for i in range(0,self.numberGraph):
                self.y.append([])

        elif self.typeGraph==True: # if x axe is like y axe
            for i in range(0,self.numberGraph):
                self.x.append([])
                self.y.append([])

        # set y axe position
        if self.ySide=="right":
            self.figure.yaxis.set_label_position("right")
            self.figure.yaxis.tick_right()
        if self.ySide=="left":
            self.figure.yaxis.set_label_position("left")
            self.figure.yaxis.tick_left()
        # set figure display parameters
        self.figure.set_title(self.title,loc='right') 
        self.figure.set_xlabel(self.titleX)
        self.figure.set_ylabel(self.titleY)
        self.figure.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
        # set axe limits
        self.figure.set_ylim(self.ylim)
        if len(self.xlim)==2:
            self.figure.set_xlim(self.xlim)

        # don't show coordonates when pasing mouse on graphe
        
class Graph3d():

    def __init__(self,fig,position,title,titleX,titleY,titleZ,xlim,ylim,zlim,typeGraph,linestyle,facecolor,graphLegend):
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
        self.typeGraph=typeGraph # True => display all points and False => display only last point
        self.graphLegend=graphLegend
        self.xlim3D = xlim
        self.ylim3D = ylim
        self.zlim3D = zlim
        self.linestyle=linestyle
        

        # don't show coordonates when pasing mouse on graphe
        self.figure.format_coord = lambda x, y: ''
    
    def animate(self): # update graphe    
           
        self.figure.cla() # Clear the current axes
        # set figure display parameters
        self.figure.set_xlabel(self.titleX)
        self.figure.set_ylabel(self.titleY)
        self.figure.set_zlabel(self.titleZ)
        # set axe limits
        self.figure.set_xlim3d(self.xlim3D)
        self.figure.set_ylim3d(self.ylim3D)
        self.figure.set_zlim3d(self.zlim3D)
        self.figure.set_title(self.title,loc='right')

        # update graph (depending graph type)
        # True => display all points and False => display only last point
        if(self.typeGraph==False):
            #self.figure.scatter(self.x[-1],self.y[-1],self.z[-1],c=self.color,linestyle='--', marker=self.marker)
            self.figure.scatter3D(self.x[-1],self.y[-1],self.z[-1],c=self.color, marker=self.marker)
            if self.linestyle!='':
                self.figure.plot3D([self.x[-1], 0], [self.y[-1], 0], [self.z[-1], 0],self.color,linestyle=self.linestyle)

        else:
            if self.linestyle==None:
                print("mzede")
                self.figure.scatter3D(self.x,self.y,self.z,c=self.color, marker=self.marker)
            #self.figure.plot3D([self.x[-1], self.x[len(self.x)-2]], [self.y[-1], self.y[len(self.y)-2]], [self.z[-1], self.z[len(self.z)-2]],c=self.color, marker=self.marker)            
            else:
                self.figure.plot3D(xs=self.x,ys=self.y,zs=self.z,linestyle=self.linestyle, marker=self.marker)

    def initGraph(self):
        self.figure.cla()
        self.x=[]
        self.y=[]
        self.z=[]
        # set figure display parameters
        self.figure.set_title(self.title,loc='right') 
        self.figure.set_xlabel(self.titleX)
        self.figure.set_ylabel(self.titleY)
        self.figure.set_zlabel(self.titleZ)
        # set axe limits
        self.figure.set_xlim3d(self.xlim3D)
        self.figure.set_ylim3d(self.ylim3D)
        self.figure.set_zlim3d(self.zlim3D)
        self.figure.view_init(azim=-60)

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
        self.numberGraph=10
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
        self.figure.set_ylim(self.ylim)
        self.position=np.arange(4)
        y=[0,100,2000,15000]
        self.figure.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
        self.figure.bar(self.position, np.array(self.y), color=self.color, edgecolor='black')
        self.figure.set_xticks(self.position)
        self.figure.set_xticklabels(self.x) 

    def initGraph(self):
        self.figure.cla()
        self.y=[]
        for i in range(0,self.numberGraph):
            self.y.append([])
