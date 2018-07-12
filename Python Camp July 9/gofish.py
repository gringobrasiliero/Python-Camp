from random import randint
face_card = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck = []
hHand = []
cHand = []
cards_left = 51
for i in face_card:
    deck.append(i)
    deck.append(i)
    deck.append(i)
    deck.append(i)


def set_game():
    global cards_left
    global hHand
    global cHand
    x = 1
    while x <= 7:
        random_card = randint(0,cards_left)
        hHand.append(deck[random_card])
        deck.pop(random_card)
        cards_left -= 1
        x += 1
    x = 1
    while x <= 7:
        random_card = randint(0,cards_left)
        cHand.append(deck[random_card])
        deck.pop(random_card)
        cards_left -= 1
        x += 1





def game():

    set_game()


