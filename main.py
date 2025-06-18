"""projekt_1.py: první projekt do Engeto Online Python Akademie

author: Petra Jancarova
email: p.jancarova@gmail.com
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

finalnitext = "-------------------------------------------"
import time
regusers = {'bob':'123', 'ann':'pass123', 'mike':'password123', 'liz':'pass123'}
#vstup zalogovani se
username = input("username:")
for login, heslo in regusers.items():
    if username == login: 
        heslovicko = input("password:")
        print(finalnitext)
        if heslovicko == heslo:
            #vybrat mezi 3 texty v promenne
            introd = f"Welcome to the app, {username}" + "\n" + "We have 3 texts to be analyzed.\n"+ finalnitext
            print(introd)
            txtchoice = input("Enter a number btw. 1 and 3 to select: ")
            if txtchoice.isdigit():
                print(finalnitext)
                txtchoice = int(txtchoice)
                if txtchoice in range(1, 4):
                    #dat promennou pro ty 3 ciselny moznosti
                    if txtchoice == 1:
                        TEXTIND = TEXTS[0]
                    elif txtchoice == 2:
                        TEXTIND = TEXTS[1]
                    elif txtchoice == 3:
                        TEXTIND = TEXTS[2]
                    #spocitani poctu slov
                    slova = TEXTIND.split()
                    pocetslov = len(slova)
                    print(f"There are {pocetslov} words in the selected text.")
                    #pocitani SLOV (ne zvlast pismen) co jenom zacinaj velkym..
                    pocetcap = 0
                    for slovo in TEXTIND.split():
                        if slovo[0].isupper() and slovo[1].islower():
                            pocetcap += 1
                    print(f"There are {pocetcap} titlecase words.")
                    #pocitani slov co jsou CELE z velkych pismen..
                    pocetupper = 0
                    for slovo in TEXTIND.split():
                        if slovo[0].isupper() and slovo[1].isupper():
                            pocetupper += 1
                    print(f"There are {pocetupper} uppercase words.")
                    #pocitani slov co jsou CELE z malych pismen
                    pocetlower = 0
                    for slovo in TEXTIND.split():
                        if slovo.islower():
                            pocetlower += 1
                    print(f"There are {pocetlower} lowercase words.")
                    #pocitani slov co jsou cisla..
                    pocetcisel = 0
                    for cislo in TEXTIND.split():
                        if cislo.isnumeric():
                            pocetcisel += 1
                    print(f"There are {pocetcisel} numeric strings.")
                    #soucet tech cisel...
                    hodnotacisel = 0
                    listcisla = []
                    for cislo in TEXTIND.split():
                        if cislo.isnumeric():
                            listcisla.append(int(cislo))     
                    print("The sum of all the numbers ", sum(listcisla), "\n", finalnitext, "\n", "LEN|      OCCURENCES      |NR.", "\n", finalnitext)

                    #graf pro soucet pismen ve slovech
                    vypis = []
                    for slova in TEXTIND.split():
                        vypis.append(len(slova))
                    for cisl in set(vypis):
                        print(f"{cisl:>2}| {"*"*vypis.count(cisl):25}|{str(vypis.count(cisl)).lstrip()}")
                    time.sleep(60)
                else:
                    print("Daný text není dostupný. Program bude ukončen.")
                    time.sleep(3)
            else:
                print("Zadejte celé číslo 1-3")
                time.sleep(3)
            break
        else:
            print(f"username:{username}\npassword:{heslovicko}\nunregistered user, terminating the program..")
            time.sleep(3)
            break
else:
    heslovicko = input("Zadejte prosím Vaše heslo:")
    print(f"username:{username}\npassword:{heslovicko}\nunregistered user, terminating the program..")
    time.sleep(3)
