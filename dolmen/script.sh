#!/bin/bash
LOG_TYPE="INFO"
LOCATION="/home/axeln/hermin-I/dolmen/python"
NAME="trame.txt"
UPDATE_DELAY="200"
LOG_FILE='dolmen.log'
SAVE_REPORT_FOLDER="SaveSession"
THEME="normal"
CSV="report.csv"
CONFIG_TXT="config.txt"
NAME_SAVE_FIGURE='report.png'
ROCKET_NAME="HerminI"

init=$(python Init.py 2>&1) 

testcmd () {
    command -v "$1" >/dev/null
}
            
if testcmd xterm; then
    if [[ -z $init ]]
    then        
        make &
        FILE="prog"
        if test -f "$FILE"; then
            echo "$FILE exist"
            xterm -e ./prog  $CONFIG_TXT $CSV   &  
            python Main.py $LOG_TYPE $LOCATION $NAME $UPDATE_DELAY $LOG_FILE $SAVE_REPORT_FOLDER $CSV $NAME_SAVE_FIGURE $CONFIG_TXT $THEME $ROCKET_NAME                      
        fi
        else             
            echo "Error when compiling c++ code please check the c++ code"
        fi
    else
        echo $init
        echo "Exit"
    fi