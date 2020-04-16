#IMPORT
import machine
import SerialSDLib
import pycom
import time

pycom.heartbeat(False)
uart_sd = machine.UART(0,baudrate=9600,pins=('P1','P0'))
resetOpenLogPin = Pin('P20', mode=Pin.OUT)

SerialSDLib.SetupOpenLog(uart_sd,resetOpenLogPin)

fileName = "fichier_data.txt"

SerialSDLib.createFile(uart_sd,fileName)

uart_sd.write("Test ")
uart_sd.write("De la carte")
uart_sd.write(" SD")
uart_sd.write("\n")
uart_sd.write("test1")
uart_sd.write("\n")
uart_sd.write("\n")
uart_sd.write("test2")
uart_sd.write("\n")
uart_sd.write("$GPRMC,170234.000,A,4821.7252,N,00434.0044,W,1.74,192.90,270220,,,A*75")

while 1:
    pycom.rgbled(0x002000)
    time.sleep(0.5)
    pycom.rgbled(0x000000)
    time.sleep(0.5)
