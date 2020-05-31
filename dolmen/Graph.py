#import python Module
import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.markers as marker


class Graph():

    def __init__(self,x,y,row,column,width,height,colorText,xColor,yColor,axeLabelColor,gridColor,colorFont):

        #size
        self.x=x
        self.y=y

        #position in windows
        self.row=row
        self.column = column

        #size 
        self.width=width
        self.height=height

        #color
        self.colorFont=colorFont
        self.colorText=colorText
        self.xColor=xColor
        self.yColor=yColor
        self.axeLabelColor=axeLabelColor
        self.gridColor=gridColor

        #create figure
        self.figure = plt.figure(figsize=(self.x,self.y),constrained_layout=False,facecolor=self.colorFont)

        #initialise figure parameters
        matplotlib.rcParams['text.color'] = self.colorText
        matplotlib.rcParams['xtick.color'] = self.xColor
        matplotlib.rcParams['ytick.color'] = self.yColor
        matplotlib.rcParams['axes.labelcolor'] = self.axeLabelColor
        matplotlib.rcParams['grid.color'] = self.gridColor

        #Create figure grid
        self.grid= self.figure.add_gridspec(nrows=self.row, ncols=self.column, width_ratios = self.width, height_ratios = self.height,wspace = 0.5,hspace=0.5)
        #frame file to decode
        self.file = None


    #adding graph in figure    
    def addToWindows(self,windows,rowGraph,columnGraph,columnspan,rowspan,rowToolbar,columnToolbar):

        #define graphe variables
        self.windows = windows

        #graphe position
        self.rowGraph=rowGraph
        self.columnGraph=columnGraph

        #number of column
        self.columnspan=columnspan
        self.rowspan=rowspan
        #matplotlib tool position
        self.rowToolbar=rowToolbar
        self.columnToolbar=columnToolbar

        #create canva to display graph
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.windows)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas._tkcanvas.grid(row=self.rowGraph, column=self.columnGraph,columnspan=self.columnspan,rowspan=self.rowspan,ipadx=1,ipady=1,padx=1,pady=1,sticky="w")
        
        # matplot tools
        # add matplot tools
        self.toolbarFrame = tk.Frame(self.windows)
        self.toolbarFrame.grid(row=self.rowToolbar,column=self.columnToolbar)
        toolbar = NavigationToolbar2Tk( self.canvas, self.toolbarFrame)
        #config toolbar
        toolbar.config(background=self.colorFont)
        toolbar.update()        
    
    # function to save figure
    def saveFig(self,SAVE_REPORT_FOLDER,NAME_SAVE_FOLDER,NAME_SAVE_FIGURE):
        self.figure.savefig(SAVE_REPORT_FOLDER + '/' + NAME_SAVE_FOLDER + '/' + NAME_SAVE_FIGURE,facecolor=self.colorFont,edgecolor=self.colorText)
        

class GraphPlot(): # 2D Graphe

    def __init__(self,fig,position,title,titleX,titleY,xlim,ylim,facecolor,graphLegend,ySide,typeGraph):

        #create graph in figure
        self.fig=fig
        self.facecolor=facecolor #background color        
        self.figure = self.fig.figure.add_subplot(position,facecolor=self.facecolor)

        #color
        self.color = [] 
        self.graphLegend=graphLegend

        #graph name 
        self.title=title
        self.titleX=titleX
        self.titleY=titleY

        #axes limits
        self.xlim=xlim
        self.ylim=ylim

        #axes
        self.x=[]
        self.y=[]

        #graph type
        self.typeGraph=typeGraph # False x axe = time and True = x axe is like y axe

        #number of graph
        self.numberGraph=0  

        #label (legend text)
        self.label=[]

        #position of y axe
        self.ySide=ySide

        # don't show coordonates when passing mouse on graphe
        self.figure.format_coord = lambda x, y: ''

    #function to update graph
    def animate(self):  

        self.figure.cla() # Clear the current axes
        
        # set figure display parameters
        self.figure.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
        self.figure.set_title(self.title,loc='right') 
        self.figure.set_xlabel(self.titleX)
        self.figure.set_ylabel(self.titleY)

        # set axes limits
        if len(self.ylim)==2:
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

        # if x axe isn't time axe
        if self.typeGraph==True:

            for i in range(0,self.numberGraph):

                if len(self.label) == self.numberGraph: # if label to display
                    self.figure.plot(self.x[i], self.y[i],color = self.color[i],label =str(self.label[i]), marker='o') # + " = " + str(self.y[i][-1])
                    self.figure.legend(facecolor=self.graphLegend,loc="upper left")

                else :
                    self.figure.plot(self.x[i], self.y[i],color = self.color[i], marker='o')

    #function to initing graph                                    
    def initGraph(self):

        self.figure.cla()# Clear the current axes

        #axes
        self.x=[]
        self.y=[]

        if self.typeGraph==False: # if x axe is time
            for i in range(0,self.numberGraph):
                self.y.append([])

        elif self.typeGraph==True: # if x axe isn't time axe
            for i in range(0,self.numberGraph):
                self.x.append([])
                self.y.append([])

        # set axes position
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

        # set axes limits
        if len(self.ylim)==2:
            self.figure.set_ylim(self.ylim)
        if len(self.xlim)==2:
            self.figure.set_xlim(self.xlim)

        
        
class Graph3d():

    def __init__(self,fig,position,title,titleX,titleY,titleZ,xlim,ylim,zlim,typeGraph,linestyle,facecolor,graphLegend):

        #create graph
        self.facecolor=facecolor
        self.figure = fig.figure.add_subplot(position,projection='3d',facecolor=self.facecolor)
        self.linestyle=linestyle

        #axes
        self.x=[]
        self.y=[]
        self.z=[]

        #color 
        self.color =None
        self.graphLegend=graphLegend

        #graph name 
        self.title=title
        self.titleX=titleX
        self.titleY=titleY
        self.titleZ=titleZ

        #marker
        self.marker=None
        
        #graph type
        self.typeGraph=typeGraph # True => display all points and False => display only last point
        
        #axes limits
        self.xlim3D = xlim
        self.ylim3D = ylim
        self.zlim3D = zlim

        
        # don't show coordonates when passing mouse on graphe
        self.figure.format_coord = lambda x, y: ''
    
    #function to update graph
    def animate(self):   
           
        self.figure.cla() # Clear the current axes

        # set figure display parameters
        self.figure.set_xlabel(self.titleX)
        self.figure.set_ylabel(self.titleY)
        self.figure.set_zlabel(self.titleZ)

        # set axes limits
        self.figure.set_xlim3d(self.xlim3D)
        self.figure.set_ylim3d(self.ylim3D)
        self.figure.set_zlim3d(self.zlim3D)
        self.figure.set_title(self.title,loc='right')

        # update graph (depending graph type)
        # True => display all points and False => display only last point
        if(self.typeGraph==False):

            self.figure.scatter3D(self.x[-1],self.y[-1],self.z[-1],c=self.color, marker=self.marker)

            if self.linestyle!=None:
                self.figure.plot3D([self.x[-1], 0], [self.y[-1], 0], [self.z[-1], 0],self.color,linestyle=self.linestyle)

        else:

            if self.linestyle==None:
                self.figure.scatter3D(self.x,self.y,self.z,c=self.color, marker=self.marker)

            else:
                self.figure.plot3D(xs=self.x,ys=self.y,zs=self.z,linestyle=self.linestyle, marker=self.marker)


    #function to initing graph 
    def initGraph(self):

        self.figure.cla()# Clear the current axes
        #axes
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
