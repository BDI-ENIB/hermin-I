import sys

if (sys.version_info < (3, 0)):
    sys.exit("You must install python 3")
try:
    import tkinter
except ImportError:
    sys.exit("tkinter isn't installed") 
   
try:
    import matplotlib
except ImportError:
    sys.exit("matplotlib isn't installed") 

try:
    import numpy
except ImportError:
    sys.exit("numpy isn't installed") 

