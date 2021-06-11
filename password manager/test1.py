import getpass
import pickle
import random

import pyperclip

info = {}

#passwort
s = "abcdefghijklmnopqrstuvwxyz0123456789ABDEFEGHIJKLMONOPQRSTUVZYZ"
len_password = getpass.getpass(input("Gib an wie viele buchstaben/zahlen password haben soll:"))
password = "".join(random.sample(s, len_password))
print(password)

#----------------------------
antwort = input("Möchtest du dieses Passwort behalten?")
if ("ja" in antwort):
        account_name = input("Gib Account Name ein: ")
        info[account_name] = password
        with open("yunus.pw", "bw") as filewrite:
            pickle.dump(info, filewrite, protocol=2)

else:
    print("ok")

#### wahl2

m_password= input("Master passwprd")

if(m_password=="yunusemre"):
    account_name=input("enter account name:")
    with open("yunus.pw","br") as readfile:
        info= pickle.load(readfile)

        if account_name in info:
            pyperclip.copy(info[account_name])
            print("password copied")
