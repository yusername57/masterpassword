import maskpass
from cryptography.fernet import Fernet
import threading

def ueberpruefeGleichheit(passwort):
    pruefer = maskpass.advpass("Geben sie ihr passwort erneut ein")
    if (passwort == pruefer):
        print("akzeptiert")
        passwortVerstauen(passwort)

    elif (passwort!= pruefer):
        print("Die Eingabe hat nicht übereingestimmt mit der zuvor, auf ein neues")
        passwortBestimmen()

        #passwort = ""
        #passwortBestimmen2(passwort)


def passwortVerstauen(passwort):
    key = Fernet.generate_key()
    crypter = Fernet(key)
    with open('key.txt', 'wb') as file:

        file.write(key)


    bPW = bytes(passwort, 'utf8')
    with open('passwort.txt', 'wb') as file:
        file.write(crypter.encrypt(bPW))


def ueberpruefePasswortLaenge(passwort):
    while passwort.__len__() < 7:
        passwort = maskpass.advpass("Zu kurz!\n"
                                    "Geben sie hier ihr Passwort ein(länger als 7 Zeichen).\n"
                                    "WICHTIG! Schreiben sie für ein sicheres einen unüblichen Satz auf ein Blatt Papier, wie Z.B:\n"
                                    "Fuchs jagen Tier Baum Zähne Edelstahl\n"
                                    "Nun wählen sie jedes dritte Zeichen für ihr Passwort(NICHT der Beispielsatz)\n")
    return passwort


def pruefExistPassW():
    tester=False
    try:
        f=open('key.txt')
        t1=open('passwort.txt')

        tester=True
    except Exception:
        print("Noch kein Passwort erstellt")
    if tester==True:
        pwEinlesenVonTextData()
    elif tester==False:
        passwortBestimmen()






def pwEinlesenVonTextData():
    print("Es gibt bereits ein Passwort")
    #pwEingabe = maskpass.advpass("Geben sie ihr Passwort ein um fortzufahren")
    #bPwEingabe=bytes(pwEingabe,"utf-8")

    with open('key.txt', 'rb') as file:
        key = file.read()
        crypter = Fernet(key)

    with open('passwort.txt', 'rb') as file:
        pw = file.read()
        decryptetPW = crypter.decrypt(pw)
    '''if (decryptetPW==bPwEingabe):
        print("richtige Eingabe")
        menuFuerPwOptionen()'''
    pwEingabeBeiProgrammStart(decryptetPW)


def pwEingabeBeiProgrammStart(decryptetPW):
    x = 3
    while x > 0:
        pwEingabe = maskpass.advpass("Geben sie ihr Passwort ein um fortzufahren " + str(x) + " Versuch/e verbleibend")
        bPwEingabe = bytes(pwEingabe, "utf-8")
        if (bPwEingabe == decryptetPW):
            print("richtige Eingabe")
            menuFuerPwOptionen()
            x = 0
        x = x - 1


def menuFuerPwOptionen():
    optionen = maskpass.advpass("Falls sie ihr passwort anzeigen wollen, drücken sie die 1\n"
                                "Falls sie ihr passwort ändern wollen, drücken sie die 2\n"
                                "Falls sie das programm beenden wollen, drücken sie die 3\n"
                                )

    if(optionen=='2'):
        fileKey = r"C:\Users\Arvand\PycharmProjects\Uni1\tester\key.txt"
        filePassW=r"C:\Users\Arvand\PycharmProjects\Uni1\tester\passwort.txt"
        ##os.remove(fileKey)
        ##os.remove(filePassW)
        passwortBestimmen()
    elif(optionen=='3'):
        print("Programm beendet")
        exit()
def dummePWdaTa():
    fopen= open("liste.txt", 'r')
    string1="prettyface"
    s=" "
    L=s.split()
    while(s):
        s=fopen.readline()
        if string1 in L:
            print("gibt ws")

    '''fopen= open("liste.txt",mode='r+')
    fread=fopen.readlines()
    passwort = maskpass.advpass("Geben sie hier ihr Passwort ein(länger als 7 Zeichen).\n"
                                   "WICHTIG! Schreiben sie für ein sicheres Passwort zunächst einmal einen unüblichen Satz auf ein Blatt Papier, wie Z.B:\n"
                                   "Fuchs Eisladen Krone Baum Zähne Edelstahl\n"
                                   "Nun wählen sie jedes dritte Zeichen für ihr Passwort(NICHT der Beispielsatz, sondern e)")
    for line in fread:
        if passwort in line:
            print("identischhhh")
            passwortBestimmen()'''


def sicherheitsTest(passwort):
    fopen= open('liste.txt', 'r')
    fread= fopen.readlines()

    pwTest=True
    while(pwTest==True):
        pw= str(passwort)
        pw.lower()
        for line in fread:

            if pw in line:
                return True
                break
        pwTest=False
    return False

def passwortBestimmen():
    #dummePWdaTa()
    passwort = maskpass.advpass("Geben sie hier ihr Passwort ein(länger als 7 Zeichen).\n"
                                "WICHTIG! Schreiben sie für ein sicheres Passwort zunächst einmal einen unüblichen Satz auf ein Blatt Papier, wie Z.B:\n"
                                "Fuchs Eisladen Krone Baum Zähne Edelstahl\n"
                                "Nun wählen sie jedes dritte Zeichen für ihr Passwort(NICHT der Beispielsatz, sondern einen selbstgewählten Satz)\n")
    if sicherheitsTest(passwort):
        print("Nicht sicher genug,anderes Passwort wählen!")
        passwortBestimmen()

    ueberpruefePasswortLaenge(passwort)
    sicherheitsTest(passwort)
    ueberpruefeGleichheit(passwort)
    # passwortaendern(passwort)

pruefExistPassW()

