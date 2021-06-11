
def check(schwaches_passwort):

    ok="n"
    while ok == "n":
        passwort=input("Gib pw ein:")

        if passwort not in schwaches_passwort:
            print("Passwort erfolgreich")
            ok = "y"
            break
        else:
            schwaches_passwort==passwort
            print("Schwaches Passwort")

        return passwort

####### An der Stelle schwaches_passwort müsste die textdatei mit den inhalten(123456,blabla) sein
schwaches_passwort = "hallo"
gutes_passwort=check(schwaches_passwort)