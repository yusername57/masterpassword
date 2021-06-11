from builtins import print

from cryptography.fernet import Fernet


def storagePasswortInData(passwort):
    antwort = input("Möchtest du dieses Passwort behalten?")
    if ("ja" in antwort):
        with open("yunuspw.txt") as file:
            file.read()


def ueberpruefeGleichheit(passwort):
    pruefer = input("Geben sie ihr passwort erneut ein")
    if (passwort == pruefer):
        print("akzeptiert")
        storagePasswortInData(passwort)

    else:
        passwort = ""
        passwortBestimmen2(passwort)


def enycrpt(key):
    f = Fernet(key)


def ueberpruefePasswort(passwort):
    while passwort.__len__() < 7:
        passwort = input("Zu kurz!\n"
                         "Geben sie hier ihr Passwort ein(länger als 7 Zeichen).\n"
                         "WICHTIG! Schreiben sie für ein sicheres einen unüblichen Satz auf ein Blatt Papier, wie Z.B:\n"
                         "Fuchs jagen Tier Baum Zähne Edelstahl\n"
                         "Nun wählen sie jedes dritte Zeichen für ihr Passwort(NICHT der Beispielsatz)\n")
    return passwort


def passwortaendern(passwort):
    x = True
    while (x):
        passwortFrage = input("Wollen sie ihr Passwort ändern ? ja ODER nein angeben Bitte")
        if passwortFrage.__eq__("ja"):
            wort2 = input("Geben sie ein neues Passwort ein")
            ueberpruefePasswort(wort2)

        elif passwortFrage.__eq__("nein"):

            print(passwort)

            x = False


def passwortBestimmen():
    passwort = input("Geben sie hier ihr Passwort ein(länger als 7 Zeichen).\n"
                     "WICHTIG! Schreiben sie für ein sicheres Passwort zunächst einmal einen unüblichen Satz auf ein Blatt Papier, wie Z.B:\n"
                     "Fuchs jagen Krone Baum Zähne Edelstahl\n"
                     "Nun wählen sie jedes dritte Zeichen für ihr Passwort(NICHT der Beispielsatz, sondern einen selbstgewählten Satz)\n")
    ueberpruefePasswort(passwort)
    ueberpruefeGleichheit(passwort)
    passwortaendern(passwort)


def passwortBestimmen2(passwort):
    passwort = input("Die eingabe hat nicht übereingestimmt mit der zuvor, auf ein neues\n"
                     "Geben sie hier ihr Passwort ein(länger als 7 Zeichen).\n"
                     "WICHTIG! Schreiben sie für ein sicheres Passwort zunächst einmal einen unüblichen Satz auf ein Blatt Papier, wie Z.B:\n"
                     "Fuchs jagen Krone Baum Zähne Edelstahl\n"
                     "Nun wählen sie jedes dritte Zeichen für ihr Passwort(NICHT der Beispielsatz, sondern einen selbstgewählten Satz)\n")
    ueberpruefePasswort(passwort)
    ueberpruefeGleichheit(passwort)
    passwortaendern(passwort)


passwortBestimmen()
