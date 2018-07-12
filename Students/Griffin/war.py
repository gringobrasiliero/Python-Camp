from random import randint
face_cards = [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck = []
for i in face_cards:
    deck.append(i)
    deck.append(i)
    deck.append(i)
    deck.append(i)

hHand = []
cHand = []



def draw():
    global hTurn
    global cTurn
    randomCard  = randint(0,51)
    hTurn = deck[randomCard]
    randomCard  = randint(0,51)
    cTurn = deck[randomCard]

    print("Human: " + hTurn)
    print("CPU: " + cTurn)


draw()
def test():
    if hTurn > cTurn:
        print("Human won.")
        hHand.append(hTurn)
        hhand.append(cTurn)
    elif hTurn < cTurn:
        print("CPU won.")
        hHand.append(hTurn)
        hHand.append(cTurn)
    else:
       print("Draw")
       hHand.append(hTurn)
       cHand.append(cTurn)



print(hHand)
print(cHand)

def game():
