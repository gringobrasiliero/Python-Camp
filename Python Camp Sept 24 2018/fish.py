
from random import shuffle

face = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
deck = []
hHand = []
cHand = []

def createDeck():
    for i in range(13):
        deck.append(face[i])
        deck.append(face[i])
        deck.append(face[i])
        deck.append(face[i])
    shuffle(deck)

def drawStart():
    for i in range(7):
        hHand.append(deck[0])
        deck.pop(0)
        cHand.append(deck[0])
        deck.pop(0)

def hTurn():
    x = 0
    guess = input("Your turn.")
    z = 0
    if z == 0:
        for i in cHand:
            if i == guess:
                print("Computer has a " + i)
                hHand.append(i)
                cHand.pop(x)
                x = x - 1
                z =1
            x = x + 1
    if z == 0:
        print("Go Fish")
    elif z == 1:
        hTurn()


def cTurn():
    x = 0
    guess = input("Your turn.")
    z = 0
    if z == 0:
        for i in hHand:
            if i == guess:
                print("Computer took your " + i)
                cHand.append(i)
                hHand.pop(x)
                x = x - 1
                z =1
            x = x + 1
    if z == 0:
        print("Go Fish")
    elif z == 1:
        cTurn()




def game():
    createDeck()
    drawStart()
    while True:
        hTurn()
        print(hHand)
        print(cHand)

game()

