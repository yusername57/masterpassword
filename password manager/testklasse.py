def abc():
    fopen= open('liste.txt', 'r')
    fread= fopen.readlines()

    pwTest=True
    while(pwTest==True):
        pw= "1234"

        for line in fread:

            if pw in line:
                return True
                break
        pwTest=False
    return False

if abc():
    print("karamba")