from machine import ADC
import os
import time
adc = ADC(0)
#adc_c = adc.channel(pin='P13',attn=ADC.ATTN_6DB) #pour une pile de 1.259V , print(adc_c.value()) donne 2520
adc_c = adc.channel(pin='P13',attn=ADC.ATTN_0DB) #pour une pile de 0.629V , print(adc_c.value()) donne 2070

def createFile(nom):
    nom = nom+(".txt")
    file = open(nom,"w")
    return file

def writeFile(data,file):
    file.write(str(data)+("\n"))
    return

file = createFile("save3")

for  i in range(1000):
    adc_c()
    tension_thermi = adc_c.value()
    print(tension_thermi)
    writeFile(str(tension_thermi),file)
    time.sleep(0.2)

file.close()
