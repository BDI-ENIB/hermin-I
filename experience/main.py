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
pycom.heartbeat(False)
liste_capteur = {} #dictionnaire qui stoque la fréquence d'enregistrement et la marche à suivre pour récuperer et enregistrer les données de chaque capteurs
#usb
uart_pc = machine.UART(0, 115200)
os.dupterm(uart_pc)
#sd
nombreLigneParFichier = 100
#gps
uart_gps = UART(1,9600)
envoyerDonneeGPS=0
def fonction_gps():
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
liste_capteur["gps"] = {"frequence":2,"fonction":fonction_gps} # ["frequence":n] => le GPS est enregistré tous les "n" cycles
#mpu
i2c = I2C(0)
sensor = MPU9250(i2c) #m/s^2, rad/s and uT
def fonction_mpu():
    mpu_str = str('acc'+str(sensor.acceleration)+'gyro'+str(sensor.gyro)+'mag'+str(sensor.magnetic))
    print(mpu_str)
    writeFile(mpu_str,file)
liste_capteur["mpu"] = {"frequence":1,"fonction":fonction_mpu}
#thermistance 1
adc_1 = machine.ADC(0)
adc_c1 = adc.channel(pin='P13',attn=machine.ADC.ATTN_0DB) #pour une pile de 0.629V , print(adc_c.value()) donne 2070
def fonction_thermi_1():
    adc_c1()
    tension_thermi_1 = adc_c1.value()
    print(tension_thermi_1)
    writeFile(str(tension_thermi_1),file)
liste_capteur["thermi_1"] = {"frequence":1,"fonction":fonction_thermi_1}
#thermistance 2
adc_2 = machine.ADC(0)
adc_c2 = adc.channel(pin='P16',attn=machine.ADC.ATTN_0DB) #pour une pile de 0.629V , print(adc_c.value()) donne 2070
def fonction_thermi_2():
    adc_c2()
    tension_thermi_2 = adc_c2.value()
    print(tension_thermi_2)
    writeFile(str(tension_thermi_2),file)
liste_capteur["thermi_2"] = {"frequence":1,"fonction":fonction_thermi_2}
#capteur pression 1
adc_3 = machine.ADC(2)
adc_c3 = adc.channel(pin='P14',attn=machine.ADC.ATTN_0DB) #pour une pile de 0.629V , print(adc_c.value()) donne 2070
def fonction_pression_1():
    adc_c3()
    tension_pression_1 = adc_c3.value()
    print(tension_pression_1)
    writeFile(str(tension_pression_1),file)
liste_capteur["pression_1"] = {"frequence":1,"fonction":fonction_pression_1}
#capteur pression 2
adc_4 = machine.ADC(2)
adc_c4 = adc.channel(pin='P17',attn=machine.ADC.ATTN_0DB) #pour une pile de 0.629V , print(adc_c.value()) donne 2070
def fonction_pression_1():
    adc_c4()
    tension_pression_2 = adc_c4.value()
    print(tension_pression_2)
    writeFile(str(tension_pression_2),file)
liste_capteur["pression_2"] = {"frequence":1,"fonction":fonction_pression_2}

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

    for capteur in liste_capteur:
        if numero_cycle % capteur["frequence"] ==0:
            capteur["fonction"]()

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
