import sys

#check if python module required

#check python version
if (sys.version_info < (3, 0)):
    sys.exit("You must install python 3")

#check if tkinter is installed
try:
    import tkinter
except ImportError:
    sys.exit("tkinter isn't installed") 

#check if matplotlib is installed   
try:
    import matplotlib
except ImportError:
    sys.exit("matplotlib isn't installed") 

#check if numpy is installed   
try:
    import numpy
except ImportError:
    sys.exit("numpy isn't installed") 

#check if PIL (Image and ImageTk) are installed 
try:
    from PIL import Image, ImageTk
except ImportError:
    sys.exit("Image or ImageTk are not installed")
