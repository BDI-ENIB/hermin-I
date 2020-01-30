import os

c=0
nom="fichier"

lesfichiers=os.listdir()


test=nom+str(c)+"-0.txt"

while test in lesfichiers:

    test=nom+str(c)+"-0.txt"
    a=0
    fichierSup=nom+str(c)+"-"+str(a)+".txt"


    while fichierSup in lesfichiers:

        os.remove(str(fichierSup))
        a=a+1

        fichierSup=nom+str(c)+"-"+str(a)+".txt"
    c=c+1
print("g fini")
print(os.listdir())
