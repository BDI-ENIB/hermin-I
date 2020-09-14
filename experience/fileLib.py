import os

#   syntaxe des fichiers :
#   |   nom des fichiers :
#   |   |   le nom des fichier est de la forme "fichier[numero de session]-[numero de fichier].txt"   exemple :"fichier4-8.txt"
#   |   |   Une nouvelle session est crée à chaque fois que la lopy redémarre
#   |   |   Lorsque la variable "numero_cycle" dépasse la variable parametre "nombreCycleParFichier", un nouveau fichier est créé, "numero fichier" augmente de 1
#   |   |
#   |   structure du fichier :
#   |   |   Entre chaque cycle il y a un saut de ligne
#   |   |   Le cycle commence par le temps depuis que la lopy est alumée (en microseconde) ( précédé par "S:")
#   |   |   Puis chaque ligne représente un capteurs
#   |   Code abréviation des capteurs :
#   |   |   "G" : gps
#   |   |   "I" : centrale inertielle
#   |   |   "T" : thermistance 1
#   |   |   "U" : thermistance 2
#   |   |   "P" : capteur de pression 1
#   |   |   "Q" : capteur de pression 1



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
