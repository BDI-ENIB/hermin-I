from tkinter import *
import Windows
import Widgets
from pylab import *
home=None
admin_mode=None
about = None
def home():
    global home, admin_mode,about
    home = Tk()
    home_interface = Windows.Windows(home,"Welcome",1000,1000)
    
    Widgets.TextToPrint(home_interface,"DOLMEN Alpha version",None)
    admin_mode_button = Widgets.ButtonDisplay(home_interface,"Admin Mode","right","black",admin,50,50)
    fire_mode_button = Widgets.ButtonDisplay(home_interface,"Fire Mode","left","black",fire,50,50)
    about_button = Widgets.ButtonDisplay(home_interface,"About","bottom","black",about,50,50)
    home_interface.mainloop()
    home_interface.destroy()


def admin():
    global home, admin_mode
    admin_mode = Tk()
    admin_mode_interface = Windows.Windows(admin_mode,"Administrator",1000,1000)
    Widgets.TextToPrint(admin_mode_interface,"Administrator Mode",None)
    test = Widgets.TextInput(admin_mode_interface,"test",None)
    test2=Widgets.Case(admin_mode_interface,"test",None,None)
    test3 = Widgets.TextInput(admin_mode_interface,"test3",None)
    tab= ["test1","test2","test3"]
    Widgets.DropdownList(admin_mode_interface,"title",None,tab)
    Widgets.TextToPrint(admin_mode_interface,"test display : uidhfgfhevbdgubgdirbht",None)
    """
    var_choix = StringVar()
    choix_rouge = Radiobutton(admin_mode, text="Rouge", variable=var_choix, value="rouge")
    choix_vert = Radiobutton(admin_mode, text="Vert", variable=var_choix, value="vert")
    choix_bleu = Radiobutton(admin_mode, text="Bleu", variable=var_choix, value="bleu")
    choix_rouge.pack()
    choix_vert.pack()
    choix_bleu.pack()
    print(var_choix.get())
    """
    admin_mode_interface.mainloop()
    admin_mode_interface.destroy()

def about():
    global home, about
    about = Tk()
    about_interface = Windows.Windows(about,"About Dolmen : ",5000,5000)

    Widgets.TextToPrint(about_interface,"""
    Timothée Allègre (t7allegr@enib.fr):

    En tant que membre du BDI depuis quelques années, et suivant le projet FUSEX depuis ses débuts, j’ai souhaité m'investir 
    dans ce projet autant que possible. J’ai rapidement tenté de formuler les besoins auxquels une telle interface pourrait 
    répondre, et ai tenté de mettre ma connaissance du projet FUSEX au profit du projet DOLMEN. Je souhaite que ce projet 
    puisse servir non seulement à notre équipe de cette année, mais aussi à d’autres équipes dans le futur, et qu’il puisse 
    vivre quelques années supplémentaires.
    """,None)

    Widgets.TextToPrint(about_interface,"""
    Nathan De Saint Just (n6desain@enib.fr):

    En tant que président du BDI depuis 2 ans et fondateur du Pôle KSP au sein de celui-ci avec Evan Roué, Il me tenait à coeur de 
    participer à ce projet que je vois ce développé depuis sa création. Avec grand espoir que tout soit opérationnelle pour la C’space 
    2020 avec le tire de la fusée avec le projet DOLMEN en base sol. Montrer qu’il marche nous permettra de le réutiliser et de la
    partager à tous les autres associations spatiales.
    """,None)

    Widgets.TextToPrint(about_interface,"""
    Axel Nougier (a7nougie@enib.fr):

    En tant que membre du BDI depuis quelques années, et suivant le projet Enigma Robotics, j’ai souhaité mettre mes connaissances à 
    profit dans le projet Dolmen afin de découvrir le Pôle KSP. Je souhaite que Dolmen soit un logiciel, simple, mais à la fois 
    robuste et modulable afin qu’il puisse être appliqué à d’autres projets et pouvoir être modifié selon d’autres besoin et être
    amélioré par d’autres personnes.
    """,None)
    Widgets.addImage(about_interface,"logos.png",BOTTOM)
    
    about_interface.mainloop()
    about_interface.destroy()


def fire():
    global home, admin_mode,about
    fire = Tk()
    fire_interface = Windows.Windows(fire,"Fire Mode",1000,1000)

    x = array([1, 3, 4, 6])
    y = array([2, 3, 5, 1])
    plot(x, y)
    show() # affiche la figure a l'ecran
    t1=np.linspace(0,5,10)
    t2=np.linspace(0,5,20)
    plot(t1, t1, 'r--', t1, t1**2, 'bs', t2, t2**3, 'g^-')
    show()
    fire_interface.mainloop()
    fire_interface.destroy()