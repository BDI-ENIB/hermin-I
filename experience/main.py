#IMPORT
import pycom
import time
import machine
#import sdcard
from machine import UART,I2C,Pin
from mpu9250 import MPU9250
from mpu6500 import MPU6500, SF_G, SF_DEG_S

#FONCTIONS
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

#INITIALISATION
#usb
uart_pc = machine.UART(0, 115200)
os.dupterm(uart_pc)
#sd
nombreLigneParFichier = 100
#gps
uart_gps = UART(1,9600)
pycom.heartbeat(False)
envoyerDonneeGPS=0
frequence_cycle_GPS = 2 #le GPS est enregistré tous les "n" cycles
#mpu
i2c = I2C(0)
sensor = MPU9250(i2c) #m/s^2, rad/s and uT
frequence_cycle_MPU = 1
#thermistance
adc = machine.ADC(0)
adc_c = adc.channel(pin='P13',attn=machine.ADC.ATTN_0DB) #pour une pile de 0.629V , print(adc_c.value()) donne 2070
frequence_cycle_thermi = 1

numeroFichier=0
numero_ligne=0

nom='fichier'
lesfichiers=os.listdir()
numeroRun=0
while nom+str(numeroRun)+str('-0.txt') in lesfichiers:
    numeroRun=numeroRun+1
    print(nom+str(numeroRun)+str('-0.txt'))

nom=str(nom+str(numeroRun))
file=createFile(nom+('-')+str(numeroFichier))
print("nouveau fichier :" , nom)
pycom.rgbled(0x000000)

periode_cycle = 200000
numero_cycle = 0

ref_time = time.ticks_us()

while True:
    start_time = time.ticks_us()
    writeFile(str(start_time),file)

    if numero_cycle % frequence_cycle_GPS == 0:
        gps_byte=uart_gps.readline()
        if envoyerDonneeGPS<=5:
            uart_gps.write(b'$PMTK314,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0*29\r\n')
            envoyerDonneeGPS=envoyerDonneeGPS+1
        if 5<envoyerDonneeGPS and envoyerDonneeGPS<10:
            uart_gps.write(b'$PMTK220,500*2B\r\n')
            envoyerDonneeGPS=envoyerDonneeGPS+1
        gps_str=str(gps_byte)
        print(gps_str)
        splited_gps_str=split(gps_str)
        if ("A"  in splited_gps_str) :
            pycom.rgbled(0x00FF00)
        writeFile(str(gps_str),file)

    if numero_cycle % frequence_cycle_MPU == 0:
        mpu_str = str('acc'+str(sensor.acceleration)+'gyro'+str(sensor.gyro)+'mag'+str(sensor.magnetic))
        print(mpu_str)
        writeFile(mpu_str,file)

    if numero_cycle % frequence_cycle_thermi ==0:
        adc_c()
        tension_thermi = adc_c.value()
        print(tension_thermi)
        writeFile(str(tension_thermi),file)

    numero_cycle +=1
    numero_ligne=numero_ligne+1
    print(numeroFichier,numero_ligne)
    if numero_ligne>=nombreLigneParFichier:
        file.close()
        numero_ligne=0
        numeroFichier=numeroFichier+1
        file=createFile(nom+str('-')+str(numeroFichier))
        pycom.rgbled(0xFFC0CB)

    writeFile("",file)

    end_time = time.ticks_us()
    sleep_time = max(0,( periode_cycle - ( end_time - start_time ) )/1000000 )
    print("wait :",sleep_time ," ; working time : "+ str(100-(100*( periode_cycle - ( end_time - start_time ) ))/periode_cycle)+"%")
    print()
    time.sleep(sleep_time )
