from random import randint
face_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck = []
hHand = []
cHand = []
hScore = 0
cScore = 0


def make_deck():
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
    global hScore
    global cScore
    fish = "go fish"
    index=0
    print("Human Score: " + str(hScore))
    print("CPU Score: " + str(cScore))
    print(hHand)
    ask = input("Your turn.")
    for i in cHand:
        if ask == i:
            fish = "no"
            print("CPU has a " + ask)
            hHand.append(i)
            cHand.pop(index)
        index +=1
    if fish == "go fish":
        print("Go Fish!")
        random_card = randint(0, amount_of_cards)
        hHand.append(deck[random_card])
        amount_of_cards -=1
        end_game()
    else:
        hMove()
def cMove():
    global cHand
    global amount_of_cards
    fish = "go fish"
    index=0
    cAmount = len(cHand)-1
    c_random= randint(0,cAmount)
    cCard = cHand[c_random]
    for i in hHand:
        if cCard == i:
            print("CPU took your " + i)
            cHand.append(i)
            hHand.pop(index)
            fish = "no"
        index +=1
    if fish == "go fish":
        print("Go Fish , Computer!")
        random_card = randint(0, amount_of_cards)
        hHand.append(deck[random_card])
        amount_of_cards -=1
        end_game()
    else:
        cMove()

def check():
    global hScore
    global hHand
    hIndex = 0
    hHand.sort()
    for i in hHand:
        if hHand.count(i) == 4:
            hScore += 1
            print("You got a point!")
            q = 1
            while q <= 4:
                hHand.pop(hIndex)
                q+=1
        hIndex += 1

def c_check():
    global cScore
    global cHand
    cHand.sort()
    cIndex = 0
    for i in cHand:
        if cHand.count(i) == 4:
            cScore += 1
            print("CPU got a point!")
            q = 1
            while q <= 4:
                cHand.pop(cIndex)
                q+=1
        cIndex += 1


def end_game():
    global amount_of_cards

    if amount_of_cards == 0:
        if hScore > cScore:
            print("You won!")
        elif cScore > hScore:
            print("CPU Won!")
        else:
            print("Tie Game.")
        again= input("Press 1 to play again.")
        if again == "1":
            game()
        else:
            exit()





def game():
    deck = []
    hScore = 0
    cScore = 0
    make_deck()
    deal()
    while True:
        check()
        hMove()
        check()
        cMove()

game()