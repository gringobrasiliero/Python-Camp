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

x = 1
while x <= 7:
    randCard = randint(0,51)
    hHand.append(deck[randCard])

    randCard = randint(0, 51)
    cHand.append(deck[randCard])
    x += 1





print(hHand)
print(cHand)
