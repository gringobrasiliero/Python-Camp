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

shuffle()

print(hHand)
print("")
print(cHand)