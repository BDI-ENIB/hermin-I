
import pycom
import time
import machine
#import sdcard
from machine import UART


def split(str):
    list=str.split(",")

    return(list)


def createFile(nom):
    nom = nom+(".txt")

    file = open(nom,"w")


    return file


def writeFile(data,file):
    file.write(str(data)+("\n"))


    return





#usb
uart_pc = machine.UART(0, 115200)
os.dupterm(uart_pc)
#gps
uart_gps = UART(1,9600)
pycom.heartbeat(False)
#sd
#sd = SPI(0, mode=SPI.MASTER, baudrate=9600, polarity=0, phase=0, pins=('P19','P20','P21'))
data=[]
print('Main start')

numeroFichier=0
nombreLigneParFichier=0

nom='fichier'
lesfichiers=os.listdir()
numeroRun=0
while nom+str(numeroRun)+str('-0.txt') in lesfichiers:
    numeroRun=numeroRun+1
    print(nom+str(numeroRun)+str('-0.txt'))


nom=str(nom+str(numeroRun))


print(nom)
file=createFile(nom+('-')+str(numeroFichier))
print("nouveau fichier")

pycom.rgbled(0x000000)

envoyerDonneeGPS=0

while True:

    gps_byte=uart_gps.readline()

    if envoyerDonneeGPS<=5:
        uart_gps.write(b'$PMTK314,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0*29\r\n')
        envoyerDonneeGPS=envoyerDonneeGPS+1
    if 5<envoyerDonneeGPS and envoyerDonneeGPS<10:
        uart_gps.write(b'$PMTK220,500*2B\r\n')
        envoyerDonneeGPS=envoyerDonneeGPS+1




    gps_str=str(gps_byte)
    print(gps_str)

    select_line=gps_str.find('$GPRMC')

    data=split(gps_str)




    if select_line == 2 :

        if ("A"  in data) :
            pycom.rgbled(0x00FF00)

        writeFile(str(gps_str+"\n"),file)
        nombreLigneParFichier=nombreLigneParFichier+1
        print(numeroFichier,nombreLigneParFichier)
        if nombreLigneParFichier>=10:
            file.close()
            nombreLigneParFichier=0
            numeroFichier=numeroFichier+1
            file=createFile(nom+str('-')+str(numeroFichier))
            pycom.rgbled(0xFFC0CB)





    time.sleep(0.5)
