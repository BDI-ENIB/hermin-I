#IMPORT
import pycom
import machine
from fileLib import *
from machine import UART,I2C,Pin
from mpu9250 import MPU9250
from mpu6500 import MPU6500, SF_G, SF_DEG_S

#gps
uart_gps = UART(1,9600)
envoyerDonneeGPS=0
def fonction_gps(file):
    gps_byte=uart_gps.readline()
    init_gps()
    gps_str=str(gps_byte)
    gps_str=gps_str[2:-3]
    splited_gps_str=split(gps_str)
    if ("A"  in splited_gps_str) :
        pycom.rgbled(0x00FF00)
    writeFile(str(gps_str),file)

def init_gps():
    global envoyerDonneeGPS
    if envoyerDonneeGPS<=5:
        uart_gps.write(b'$PMTK314,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0*29\r\n')
        envoyerDonneeGPS+=1
    if 5<envoyerDonneeGPS and envoyerDonneeGPS<10:
        uart_gps.write(b'$PMTK220,500*2B\r\n')
        envoyerDonneeGPS+=1

#mpu
i2c = I2C(0)
sensor = MPU9250(i2c) #m/s^2, rad/s and uT
def fonction_mpu(file):
    mpu_str = str('a'+str(sensor.acceleration)+'g'+str(sensor.gyro)+'m'+str(sensor.magnetic))
    writeFile(mpu_str,file)

#thermistance 1
adc = machine.ADC(0)
adc_c1 = adc.channel(pin='P13',attn=machine.ADC.ATTN_0DB) #pour une pile de 0.629V , print(adc_c.value()) donne 2070
def fonction_thermi_1(file):
    adc_c1()
    tension_thermi_1 = adc_c1.value()
    writeFile(str(tension_thermi_1),file)

#thermistance 2
adc_c2 = adc.channel(pin='P16',attn=machine.ADC.ATTN_0DB) #pour une pile de 0.629V , print(adc_c.value()) donne 2070
def fonction_thermi_2(file):
    adc_c2()
    tension_thermi_2 = adc_c2.value()
    writeFile(str(tension_thermi_2),file)

#capteur pression 1
adc_c3 = adc.channel(pin='P14',attn=machine.ADC.ATTN_0DB) #pour une pile de 0.629V , print(adc_c.value()) donne 2070
def fonction_pression_1(file):
    adc_c3()
    tension_pression_1 = adc_c3.value()
    writeFile(str(tension_pression_1),file)

#capteur pression 2
adc_c4 = adc.channel(pin='P17',attn=machine.ADC.ATTN_0DB) #pour une pile de 0.629V , print(adc_c.value()) donne 2070
def fonction_pression_2(file):
    adc_c4()
    tension_pression_2 = adc_c4.value()
    writeFile(str(tension_pression_2),file)


#init liste_capteur
def init_iste_capteur():
    liste_capteur = {} #dictionnaire qui stoque la fréquence d'enregistrement et la marche à suivre pour récuperer et enregistrer les données de chaque capteurs
    liste_capteur["gps"] = {"frequence":2,"fonction":fonction_gps} # ["frequence":n] => le GPS est enregistré tous les "n" cycles
    liste_capteur["mpu"] = {"frequence":1,"fonction":fonction_mpu}
    liste_capteur["thermi_1"] = {"frequence":1,"fonction":fonction_thermi_1}
    liste_capteur["thermi_2"] = {"frequence":1,"fonction":fonction_thermi_2}
    liste_capteur["pression_1"] = {"frequence":1,"fonction":fonction_pression_1}
    liste_capteur["pression_2"] = {"frequence":1,"fonction":fonction_pression_2}
    return liste_capteur
