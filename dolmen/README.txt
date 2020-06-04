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

---

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
But if you want, you can use Dolmen with the Anaconda's Python but without font size and type. Just install the Python Requirement without deactivate conda.



         
## Run Dolmen ##

Compile the c++ code if you made modification : just open a terminal and execute make


If you want to run the script with the Anaconda python or with the Linux Python, run in terminal the anaconda script version : script.sh (but with no font size and type effect with the Anaconda Python)
         
Or if you want to use the Linux Python with Anaconda installed just open terminal in Dolmen main folder and execute the start script : /scriptNoAnaconda.sh 
 
## Adding a new sensor or removing one ##        
         
            
1. Open DolMen, click on administrator mode, then create a new sensor by naming it (in this example, we'll name ou sensor 'johnson').

2. Close DolMen 

3. In the main folder, open johnson.hpp and johnson.cpp:
   - In johnson.hpp, give your sensor a number of attributes and a column identifier
   - In johnson.cpp, create the decoding function you'll need for this sensor.
   This function has a std::string as input "johnsonIdjohnsonData;", and willinsert into the data map the datas from johnson.
   You can inspire yourself from the others sensors.         

4. In dolmen.hpp, include your johnson.hpp with all the other sensors.

5. In prog.cpp, use the factory to create your new sensor. Here you'll give him the same ID you're using on the data stream.            

6. Compile the c++ by typing 'make' in a terminal opened in the dolmen folder.

7. Open the Config.py file, add your sensor in the createGraph() function.
[optionnal] 7.bis. If you want you can create another graphe for this sensor you can create it in createGraph function (don't forget to add it in the sensors list (and in the sensors_list_set_time if you create a 2D temporal graph)
[optionnal] 7.bis. If you need to add a new sensor type (anything else than 1 data + time or 2 datas + time or 3 datas + time), you'll need to create a new function to print your sensor.
If this is the case: open the file Sensors.py and add the needed function after the line 108, on the decoding() function and verifing() function.

8. Save and close all files, then open dolmen with your brand new sensor inside.


---


## About actual version: ##

Sensors:

The ksp project (with alpha version of DolMen) uses: 
 - 00 time 
 - 01 gps 
 - 02 accelerometer 
 - 03 gyroscope
 - 04 temperature 1
 - 05 temperature 2
 - 06 pressure 1
 - 07 pressure 2 
 - 08 altitude
 
 
 ## Other Informations ##
 
 You can find two frame : 
 
 one named trame.txt => clear frame with all time and data
 one named trametest.txt => frame with no time and no data sensor and no sensor => for testing Dolmen
