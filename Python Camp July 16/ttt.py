from random import randint

win_combos = [[0,1,2], [3,4,5],[6,7,8], [6,3,0], [7,4,1], [8,5,2], [0,4,8], [6,4,2]]
place = ["X", "X", "3", "4", "5", "6", "7", "8", "9"]


def winBlock():
    global a
    for i in win_combos:
        if place[i[0]] == place[i[2]] or place[i[0]] == place[i[1]] or place[i[1]] == place[i[2]]:
            for m in i:
                if place[m] != "X" and place[m] != "O":
                    place[m] = "O"
                    a = "end of turn"
                    break

def judge():
    for i in win_combos:
        if place[i[0]] == place[i[1]] and place[i[1]] == place[i[2]]:
            print(place[i[0]] + " wins!")
            game()
def board():
    print("_" + place[6] + "_|_" + place[7] + "_|_" + place[8] + "_")
    print("_" + place[3] + "_|_" + place[4] + "_|_" + place[5] + "_")
    print("_" + place[0] + "_|_" + place[1] + "_|_" + place[2] + "_")


def h_move():
    move = int(input("Your turn."))-1
    if place[move] == "X" or place[move] == "O":
        h_move()
    else:
        place[move] = "X"

def corners():
    global a
    for i in [0,2,6,8]:
        if a == "go":
            if place[i] != "X" and place[i] != "O":
                place[i] = "O"
                a = "end of turn"
                break


def c_move():
    global a
    a = "go"
    winBlock()
    corners()
    random()

def random():
    if a == "go":
        move = randint(0,8)
        if place[move] == "X" or place[move] == "O":
            random()
        else:
            place[move] = "O"


def game():
    global place
    place = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while True:
        board()
        h_move()
        judge()
        c_move()
        judge()
game()
