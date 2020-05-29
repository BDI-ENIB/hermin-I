#!/bin/bash
trap 'kill -TERM $caffeinate_pid' EXIT
#caffeinate &
caffeinate_pid=$!
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
outputString=$(python Init.py 2>&1) 

testcmd () {
    command -v "$1" >/dev/null
}
if testcmd xterm; then
    if [[ -z $outputString ]]
    then        
        #make &
        FILE="prog"
        if test -f "$FILE"; then
            echo "$FILE exist"
            xterm -e ./prog  $CONFIG_TXT $CSV   &  
            xterm -e python Main.py $LOG_TYPE $LOCATION $NAME $UPDATE_DELAY $LOG_FILE $SAVE_REPORT_FOLDER $CSV $NAME_SAVE_FIGURE $CONFIG_TXT $THEME &
            
            #trap 'kill $(jobs -p)' EXIT
            #xterm -hold -e ./prog
            #gnome-terminal -- python Main.py $LOG_TYPE $LOCATION $NAME $UPDATE_DELAY $LOG_FILE $SAVE_REPORT_FOLDER $THEME
            #xterm -hold -e python Main.py $LOG_TYPE $LOCATION $NAME $UPDATE_DELAY $LOG_FILE $SAVE_REPORT_FOLDER $THEME
            
        fi
        else 
            echo "Error when compiling c++ code please check the c++ code"
        fi
    else
        echo $outputString
        echo "Exit"
    fi
else
    echo 'xterm is not in the path'
fi
