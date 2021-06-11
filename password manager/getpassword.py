import pickle
import pyperclip

import getpass
m_password= input("Master passwprd")

if(m_password=="yunusemre"):
    account_name=input("enter account name:")
    with open("yunus.pw","br") as readfile:
        info= pickle.load(readfile)

        if account_name in info:
            pyperclip.copy(info[account_name])
            print("password copied")