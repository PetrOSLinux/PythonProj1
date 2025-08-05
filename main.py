import time
"""project_1.py: The first Engeto Online Python Akademie Project
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

underln = "-------------------------------------------"
regusers = {'bob':'123', 'ann':'pass123', 'mike':'password123', 'liz':'pass123'}
#login entrance
username = input("username:")
for login, definpw in regusers.items():
    if username == login:
        passwd = input("password:")
        print(underln)
        if passwd == definpw:
            #pick up one of the three texts to be analyzed
            introd = f"Welcome to the app, {username}" + "\n" + "We have 3 texts to be analyzed.\n"+ underln
            print(introd)
            txtchoice = input("Enter a number btw. 1 and 3 to select: ")
            listnumbs = []
            if txtchoice.isdigit():
                print(underln)
                txtchoice = int(txtchoice)
                analys = txtchoice in range(1, 4)
                if analys:
                    #choose the specific number of it 1-3
                    if txtchoice == 1:
                        TEXTIND = TEXTS[0]
                    elif txtchoice == 2:
                        TEXTIND = TEXTS[1]
                    elif txtchoice == 3:
                        TEXTIND = TEXTS[2]
                    #wordcutting
                    textdivision = TEXTIND.split()
                    #wordcounting of all words is the same as the length of the .split() method so counting it with it
                    wdamount = len(textdivision)
                    print(f"There are {wdamount} words in the selected text.")

                    titlelt, upperlt, lowerlt, numberamount = 0, 0, 0, 0
                    for singlew in textdivision:
                    #wordcounting only the title words
                        if len(singlew) >= 2 and singlew[0].isupper() and singlew[1].islower():
                            titlelt += 1
                    #wordcounting the whole-capital words
                        if singlew.isupper():
                            upperlt += 1
                    #wordcounting lower words
                        if singlew.islower():
                            lowerlt += 1
                    #wordcounting numbers within the text and their complete amount
                        if singlew.isnumeric():
                            numberamount += 1
                            listnumbs.append(int(singlew))
                    print(f"There are {numberamount} numeric strings.")
                    print(f"There are {lowerlt} lowercase words.")
                    print(f"There are {titlelt} titlecase words.")
                    print(f"There are {upperlt} uppercase words.")
                    print("The sum of all the numbers ", sum(listnumbs), "\n", underln, "\n", "LEN|      OCCURENCES      |NR.", "\n", underln)
                    
                    #graphical visualization of the literal amounts- word lengths 
                    graphics = []
                    for wdleng in textdivision:
                        graphics.append(len(wdleng))
                    for setnr in set(graphics):
                        print(f"{setnr:>2}| {'*'*graphics.count(setnr):25}|{str(graphics.count(setnr)).lstrip()}")
                    time.sleep(5)
                    break
                else:
                    print("Such a requested piece of text is not available. The program will be closed.")
                    time.sleep(3)
                    break
            else:
                print("Provide a number 1, 2 or 3")
                time.sleep(3)
                break
        else:
            print(f"username:{username}\npassword:{passwd}\nunregistered user, terminating the program..")
            time.sleep(3)
            break
else:
    passwd = input("Please provide your password:")
    print(f"username:{username}\npassword:{passwd}\nUnregistered user, terminating the program..")
    time.sleep(3)            
exit
