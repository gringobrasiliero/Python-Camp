from random import randint
face_cards = [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck = []
h_hand = []
c_hand= []
h_score = 0
c_score = 0
for i in face_cards:
    deck.append(i)
    deck.append(i)
    deck.append(i)
    deck.append(i)

#print(deck)
def deal():
    global cards_left
    x = 0
    cards_left = 51
    while x < 20:
        card = randint(0,cards_left)
        h_hand.append(deck[card])
        deck.pop(card)
        cards_left -=1
        card = randint(0, cards_left)
        c_hand.append(deck[card])
        deck.pop(card)
        cards_left-=1
        x += 1
    print(h_hand)
    print(c_hand)


def h_turn():
    global cards_left
    global h_score
    global c_score
    check()
    h_hand.sort()
    fish = "go fish"
    index=0
    print("Human Score: " + str(h_score))
    print("CPU Score: " + str(c_score))
    print(h_hand)
    ask = input("Your turn.")
    for i in c_hand:
        if ask == i:
            fish = "no"
            print("CPU has a " + ask)
            h_hand.append(i)
            c_hand.pop(index)
        index +=1
    if fish == "go fish":
        print("Go Fish!")
        cards_left = len(deck)-1

        random_card = randint(0, cards_left)
        h_hand.append(deck[random_card])
        cards_left -=1
        end_game()
    else:
        h_turn()


def end_game():
    global cards_left
    if cards_left == 0:
        if h_score > c_score:
            print("Human Wins!")
        elif c_score > h_score:
            print("CPU Wins!")
        game()

def check():
    global h_score
    h_hand.sort()
    index = 0
    for i in h_hand:
        if h_hand.count(i) == 4:
            print("You got a point!")
            h_score +=1
            for i in range(4):
                h_hand.pop(index)
        index += 1

def ccheck():
    global c_score
    c_hand.sort()
    index = 0
    for i in c_hand:
        if c_hand.count(i) == 4:
            print("CPU got a point")
            c_score += 1
            for i in range(4):
                c_hand.pop(index)
        index += 1

def c_turn():
    global cards_left
    c_hand.sort()
    ccheck()
    fish = "go fish"
    index=0
    print(c_hand)
    ask = input("Your turn.")
    for i in h_hand:
        if ask == i:
            fish = "no"
            print("CPU Took your " + ask)
            c_hand.append(i)
            h_hand.pop(index)
        index +=1
    if fish == "go fish":
        print("Go Fish!")
        cards_left = len(deck) - 1
        random_card = randint(0, cards_left)
        c_hand.append(deck[random_card])
        cards_left -= 1
        end_game()


def game():
    deck = []
    h_hand = []
    c_hand = []
    h_score = 0
    c_score = 0
    deal()
    while True:

        h_turn()
        c_turn()

game()