from random import randint
card_num = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck = []
hHand = []
cHand = []
for i in card_num:
    deck.append("D" + i)
    deck.append("C" + i)
    deck.append("S" + i)
    deck.append("H" + i)


print(deck)
print(len(deck))



def begin():
    x = 1
    cards_left = 54
    while x <= 7:
        randCard = randint(0,cards_left)
        hHand.append(deck[randCard])
        deck.pop(randCard)
        cards_left -= 1

        randCard = randint(0, cards_left)
        cHand.append(deck[randCard])
        deck.pop(randCard)
        cards_left -= 1
        x += 1

begin()

def hMove():
    guess = input("What is your guess?")
    for i in cHand():
        if i[1:] == ""



print(hHand)
print(cHand)
