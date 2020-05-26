#!/bin/bash
LOG_TYPE="INFO"
LOCATION="/home/axeln/hermin-I/dolmen/python"
NAME="report.csv"
UPDATE_DELAY="1000"
LOG_FILE='dolmen.log'
SAVE_REPORT_FOLDER="SaveSession"
outputString=$(python Init.py 2>&1) 

testcmd () {
    command -v "$1" >/dev/null
}
if testcmd xterm; then
    if [[ -z $outputString ]]
    then    
        #konsole --hold -e python Main.py $LOG_TYPE $LOCATION $NAME $UPDATE_DELAY $LOG_FILE $SAVE_REPORT_FOLDER
        #gnome-terminal -- python Main.py $LOG_TYPE $LOCATION $NAME $UPDATE_DELAY $LOG_FILE $SAVE_REPORT_FOLDER
        xterm -hold -e python Main.py $LOG_TYPE $LOCATION $NAME $UPDATE_DELAY $LOG_FILE $SAVE_REPORT_FOLDER 
    else
        echo $outputString
        echo "Exit"
    fi
else
    echo 'xterm is not in the path'
fi