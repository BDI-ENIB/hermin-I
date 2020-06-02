--- THE PROJECT IS STILL IN ALPHA VERSION ---

### Welcome to the DolMen program ###

Designed for the space domain, the DolMen project is much more than a simple interface, it is a
complete and modular tool allowing to follow an experimental rocket from its takeoff to its
recovery, to generate detailed reports of each flight, or even to simulate the data of a launch
from an external data frame.
As ergonomic as it is simple to use, it adapts to any rocket configuration, whatever the number
and nature of the sensors, and whatever the mode of communication with the ground.

The DolMen team.

SPACE !!!!!!!



### How to use it ? ###

## Requirement ##

-   Linux system (like Debian/Ubuntu or Arch/Manjaro)

-   Python Requirement:
        
        -   tkinter https://docs.python.org/fr/3/library/tkinter.html
        
            for Debian/Ubuntu => sudo apt-get install python-tk
            for Arch/Manjaro => sudo pacman -S tk
            
        -   matplotlib https://matplotlib.org/users/installing.html
        
            python -m pip install -U matplotlib

-   Other Requirement:

         -   xterm
        
            for Debian/Ubuntu => sudo apt-get install xterm
            for Arch/Manjaro => sudo pacman -S xterm

WARNING if you have Anaconda installed you must deactivate conda (conda deactivate) before install tkinter and matplotlib and activate conda after that (conda activate) 
Because all python code runs with Anaconda python (if it is installed) and Tkinter does not run entirely (for font size and type). You must install the python dependencies with conda disabled in order to install them in the linux python (because Dolmen uses the linux python and not that of Anaconda). Then reactivate conda.


         
## Run Dolmen ##

Compile the c++ code if you made modification : just open a terminal and execute make

Just open terminal in Dolmen main folder and execute the start script : ./script.sh


If you want to run the script with the Anaconda python, run in terminal the anaconda script version : scriptAnaconda.sh (but with no font size and type effect)
         
         
         
            
        
            



