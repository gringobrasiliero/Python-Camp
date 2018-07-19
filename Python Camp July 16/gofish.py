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
    global amount_of_cards
    amount_of_cards = 51
    x = 1
    while x <= 20:
        random_card = randint(0,amount_of_cards)
        hHand.append(deck[random_card])
        deck.pop(random_card)
        amount_of_cards -= 1
        random_card = randint(0, amount_of_cards)
        cHand.append(deck[random_card])
        deck.pop(random_card)
        amount_of_cards -= 1
        x += 1


def hMove():
    global amount_of_cards
    fish = "go fish"
    index=0
    print(hHand)
    ask = input("Your turn.")
    for i in cHand:
        if ask == i:
            fish = "no"
            hHand.append(i)
            cHand.pop(index)
        index +=1
    if fish == "go fish":
        random_card = randint(0, amount_of_cards)
        hHand.append(deck[random_card])





def cMove():
    global cHand
    index=0
    cAmount = len(cHand)-1
    c_random= randint(0,cAmount)
    cCard = cHand[c_random]
    for i in cHand:
        if cCard == i:
            cHand.append(i)
            hHand.pop(index)
        index +=1



def check():
    hIndex = 0
    for i in hHand:
        if hHand.count(i) == 4:
            hScore += 1
            q = 1
            while q <= 4:
                hHand.pop(hIndex)
                q+=1
        hIndex += 1

def game():
    hScore = 0
    deal()
    check()
    hMove()
    check()
    cMove()

game()