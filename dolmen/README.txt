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

--- Prerequisites: ---

You need to have on your computer:
 - tkinter: sudo apt-get install python-tk
 - matplotlib: sudo python -m pip install -U matplotlib
 - xterm: sudo apt-get install xterm
(theses commands might not work everywhere, but you can find some information on the internet on how to get the last version of them)

--- How to use the DolMen software? ---

In the main folder project, open a terminal and execute: ./script.sh, this will run the script launching the program.
Once the program is opened, you'll access to a graphic interface, with differents menus.
The admin mode will allow you to manage sensors and graphical interface, and the fire mode willa llow you to follow your rocket in online or in offline mode.
 - If you want to run the software in offline mode, you'll have to load your .txt file containing the data of your rocket from a popup.
 - If you want to run the software in online mode, TO BE CONTINUED

 In offline mode, hit the start button to enable decoding, a popup will tell you when the decoding will be finished.

--- How to add or remove sensors? ---

1- You'll have to create them in the software interface, by giving them a name and a graphic model:
 - 2d for a sensor with data + time
 - 3d for a sensor with 3 data + time
 - gps for a sensor with 2 data + time

1.1 (optionnal)- If you need to create a new modele for this, you'll have to modify the decoding() function from the sensors.py file.

2- You'll have to go in the prog.cpp file of the cpp folder, and create a new element from the factory.
You'll also have to go in the .cpp and .hpp files of your sensor (the program will create a squeleton automatically) and modify them with how do you want your sensor to work.
In the dolmen.hpp file, insert your new sensor .hpp at the specified emplacement.

3- Compile the c++ by opening a terminal in the c++ folder and typing 'make'.

4- In the function createGraph() from the file Config.py, line 90, add your new sensors.

5- Run the script again, you'll see your new sensor on the software, and you'll be able to use it.


--- How to rescale the graphical interface? ---

In the file Config.py change the line 94: figure=Graph.Graph(13,8,3,4,[4,4,4,2],[4,2,2],colorText,xColor,yColor,axeLabelColor,gridColor,colorFont)
Here 13 and 8 represents the width and height of the interface. You can adjust theses values and launch DolMen again.