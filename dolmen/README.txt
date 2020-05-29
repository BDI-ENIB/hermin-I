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


--- How to use the DolMen software? ---

In the main folder project, you will find a script named AXEL FAUT QUE TU METTES LE NOM DE TON SCRIPT ICI.
Launch it.
 - If you want to run the software in offline mode, you'll have to specify the name and the path of your data .txt folder. AXEL FAUT QUE TU DISES OU ICI
 - If you want to run the software in online mode, you won't have to do this.

LA AXEL C'EST A TOI DE MAQUER COMMENT ON FAIT, JE NE SAIS PAS LES DETAILS DU FONCTIONNEMENT DU PYTHON, CA A PEUT ETRE CHANGE DE CE QU'IL Y A SUR LE CAHIER DES CHARGES

--- How to add or remove sensors? ---

First, you'll have to create them in the software interface, by giving them a name and an id.

Then, you'll have to go in the prog.cpp file of the cpp folder, and create a new element from the factory.
You'll also have to go in the .cpp and .hpp files of your sensor (the program will create a squeleton automatically) and modify them with how do you want your sensor to work.
In the dolmen.hpp file, insert your new sensor .hpp at the specified emplacement.

Then, you can compile the c++ by opening a terminal in the c++ folder and typing 'make'.

If you run the launching script again, you'll see your new sensor on the software, and you'll be able to use it.
