import random
import sys

value = random.randint(0, 100)
lowestNumber = 0
highestNumber = 100

def guessnumber():
    global lowestNumber
    global highestNumber
    print("Wähle eine Nummer zwischen "+ str(lowestNumber) + " und "+ str(highestNumber))
    guess = int(input(""))
    if value == guess:
        print("Herzlichen Glückwunsch, diese Zahl ist korrekt!")
        print("")
        print("Nochmal? (j/n)")
        restart = input("")
        if restart == "j" or restart == "j":
            start()
        else:
            sys.exit()


    elif value > guess:
        print("Leider nicht richtig, die Zahl ist größer")
        if guess >= lowestNumber:
            lowestNumber = guess
        else:
            print("...aber das sollte ja eigentlich klar sein?")
        guessnumber()
    else:
        print("Leider nicht richtig, die Zahl ist kleiner")
        if guess <= highestNumber:
            highestNumber = guess
        else:
            print("...aber das sollte ja eigentlich klar sein?")
        guessnumber()


def start():
    global value
    global lowestNumber
    global highestNumber
    lowestNumber = 0
    highestNumber = 100
    value = random.randint(0, 100)
    guessnumber()


guessnumber()
