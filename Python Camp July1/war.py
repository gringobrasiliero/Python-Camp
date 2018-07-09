from random import randint
from time import sleep
# Deck of cards

card_number = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

deck = []
hHand = []
cHand = []
for i in card_number:
    deck.append("S" + i)
    deck.append("H" + i)
    deck.append("C" + i)
    deck.append("D" + i)
print(len(deck))

def shuffle():
  global hHand
  global cHand
  x = 0
  left_in_deck = 51
  while x <= 25:
    card = randint(0,left_in_deck)
    hHand.append(deck[card])
    deck.pop(card)
    left_in_deck -= 1
    card = randint(0,left_in_deck)
    cHand.append(deck[card])
    deck.pop(card)
    left_in_deck -= 1
    x += 1

def turn():
    global hHand
    global cHand
    print("Human:" + hHand[0] + " CPU: " + cHand[0])

    if hHand[1:] == "J":
        hHand[0] = 11
    elif hHand[1:] == "Q":
        hHand[0] = 12
    elif hHand[1:] == "K":
        hHand[0] = 13
    elif hHand[1:] == "A":
        hHand[0] = 14
    if cHand[1:] == "J":
        cHand[0] = 11
    elif cHand[1:] == "Q":
        cHand[0] = 12
    elif cHand[1:] == "K":
        cHand[0] = 13
    elif cHand[1:] == "A":
        cHand[0] = 14
    cardA = hHand[0][1:]
    cardB = cHand[0][1:]

    print(cardA)

    if cardA > cardB:
        hHand.append(cHand[0])
        cHand.pop(0)
        hHand.append(hHand[0])
        hHand.pop(0)
        print("Human won the battle, but not the war.")
    elif cardB > cardA:
        cHand.append(hHand[0])
        hHand.pop(0)
        cHand.append(cHand[0])
        cHand.pop(0)
        print("CPU won the battle, but not the war.")
    else:
        pile = []
        pile.append(hHand[0])
        pile.append(cHand[0])
        hHand.pop(0)
        cHand.pop(0)

def game():
    shuffle()
    while True:
        turn()
        print( "Human Cards: " + str(len(hHand)) + " CPU Cards: " + str(len(cHand)))
        sleep(1)
game()