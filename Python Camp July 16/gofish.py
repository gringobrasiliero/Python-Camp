from random import randint
face_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck = []
hHand = []
cHand = []
for i in face_cards:
    deck.append(i)
    deck.append(i)
    deck.append(i)
    deck.append(i)

def deal():
    amount_of_cards = 51
    x = 1
    while x <= 7:
        random_card = randint(0,amount_of_cards)
        hHand.append(deck[random_card])
        deck.pop(random_card)
        amount_of_cards -= 1
        random_card = randint(0, amount_of_cards)
        cHand.append(deck[random_card])
        deck.pop(random_card)
        amount_of_cards -= 1
        x += 1


print(hHand)
print(cHand)