import pycom
import time
import machine
from fileLib import *
import capteurs


#initialisation lopy
pycom.heartbeat(False)
pycom.rgbled(0x110011)
#code couleur LED RGB :
#Violet : initialisation lopy
#Vert : en fonctionnement
#Bleu : création d'un nouveau fichier

#initialisation liste_capteur
#c'est un dictionnaire qui stoque pour chaque capteur :
# -sa fréquence d'appelle
# -une fonction pour récuperer et enregistrer les  données du capteur
liste_capteur = capteurs.init_iste_capteur()

#initialisation fichier
numeroFichier=0
numeroRun=0
while "fichier"+str(numeroRun)+str('-0.txt') in os.listdir():
    numeroRun=numeroRun+1
nom=str("fichier"+str(numeroRun))
file=createFile(nom+('-')+str(numeroFichier))

#Parametrage
periode_cycle = 100000 #la période d'une boucle de simulation ( en microseconde)
nombreCycleParFichier = 100 #le nombre de cylce par fichier

this_frequence = 0 ##la frequence n'est pas la meme en mode normal ou burst

numero_cycle_from_start = 0
numero_cycle=0

launch_detection_time=0 #en micro seconde (time.ticks_us())
did_launch_has_been_detected_once = False
is_in_burst_mode= False

pycom.rgbled(0x001100)
while True:
    #Debut boucle de simulation
    start_time = time.ticks_us()
    writeFile("S"+str(start_time),file)

    #appelle des fonctions des capteurs
    for capteur in liste_capteur.values():
        if is_in_burst_mode:
            this_frequence = capteur["frequence_burst"]
        else: #if is in normal mode
            this_frequence = capteur["frequence_normal"]
        if numero_cycle_from_start % this_frequence ==0:
            capteur["fonction"](file)

    if did_launch_has_been_detected_once && (time.ticks_us() - launch_detection_time)<30000:
        pycom.rgbled(0x222222)
        is_in_burst_mode=True
    else if capteurs.detect_launch(): #si on detecte le decolage de la fusee
        launch_detection_time=time.ticks_us()
        did_launch_has_been_detected_once=True
        is_in_burst_mode=False
        pycom.rgbled(0x000000)  #alors on allume la LED en blanc

    numero_cycle_from_start +=1
    numero_cycle +=1
    if numero_cycle>=nombreCycleParFichier:
        print("je vais essayer de close")
        pycom.rgbled(0x000011)
        file.close()
        numero_cycle=0
        numeroFichier=numeroFichier+1
        file=createFile(nom+str('-')+str(numeroFichier))
        pycom.rgbled(0x001100)

    writeFile("",file) #saute une ligne dans le fichier

    #Fin boucle de simulation
    end_time = time.ticks_us()
    sleep_time = max(0,( periode_cycle - ( end_time - start_time ) )/1000000 )
    print("wait :",sleep_time ," ; working time : "+ str(100-(100*( periode_cycle - ( end_time - start_time ) ))/periode_cycle)+"%")
    print()
    time.sleep(sleep_time )
