#!/bin/bash
#!/usr/bin/env python3

#define Dolmen parameters
LOG_TYPE="INFO"
LOCATION="/home/axeln/hermin-I/dolmen/python"
NAME="trame.txt"
UPDATE_DELAY="10"
LOG_FILE='dolmen.log'
SAVE_REPORT_FOLDER="SaveSession"
THEME="normal"
CSV="report.csv"
CONFIG_TXT="config.txt"
NAME_SAVE_FIGURE='report.png'
ROCKET_NAME="HerminI"
testcmd () {
    command -v "$1" >/dev/null
}
#testcmd$(conda deactivate 2>&1 )
#execute Init.py
init=$(/usr/bin/python Init.py 2>&1) 


        
if testcmd xterm; then
    if [[ -z $init ]]
    then        
        make &
        
        xterm -e ./prog  $CONFIG_TXT $CSV   & 
            
        /usr/bin/python Main.py $LOG_TYPE $LOCATION $NAME $UPDATE_DELAY $LOG_FILE $SAVE_REPORT_FOLDER $CSV $NAME_SAVE_FIGURE $CONFIG_TXT $THEME $ROCKET_NAME   
        #testcmd $(conda activate 2>&1)                 
        
    else
        echo $init
        echo "Exit"
    fi
fi