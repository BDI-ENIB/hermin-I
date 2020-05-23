#!/bin/bash
LOG_TYPE="INFO"
LOCATION="/home/axeln/hermin-I/dolmen/python"
NAME="report.csv"
UPDATE_DELAY="1000"
LOG_FILE='dolmen.log'
SAVE_REPORT_FOLDER="SaveSession"

konsole --hold -e python Main.py $LOG_TYPE $LOCATION $NAME $UPDATE_DELAY $LOG_FILE $SAVE_REPORT_FOLDER
