from random import randint
place = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
win_combos = [ [0,1,2], [3,4,5], [6,7,8], [6,3,0], [7,4,1], [8,5,2], [0,4,8], [6,4,2]]
a = "no"
def check_win():
    for i in win_combos:
        if place[i[0]] == place[i[1]] == "O" or place[i[1]] == place[i[2]] == "O" or place[i[0]] == place[i[2]] == "O":
            for j in i:
                if place[j] != "O" and place[j] != "X":
                    place[j] = "O"
                    break

def check_block():
    global a
    for i in win_combos:
        if place[i[0]] == place[i[1]] == "X" or place[i[1]] == place[i[2]] == "X" or place[i[0]] == place[i[2]] == "X":
            for j in i:
                if place[j] != "O" and place[j] != "X":
                    place[j] = "O"
                    a = "yes"
                    return a
                    break




def judge():
    for i in win_combos:
        if place[i[0]] == place[i[1]] and place[i[1]] == place[i[2]]:
            print( place[i[0]] + " Wins!")
            game()
    if turn == 9:
        game()


def hMove():
    move = int(input("Your turn."))-1
    if place[move] == "X" or place[move] == "O":
        print("Place Taken. Try again.")
        hMove()
    else:
        place[move] = "X"

def cMove():
    global a
    a = "no"
    check_win()
    check_block()
    print(a)
    if a == "no":
        random()

def random():

    move = randint(0,8)
    if place[move] == "X" or place[move] == "O":
        random()
    else:
        place[move] = "O"


def board():
    print("_" + place[6] + "_|_" + place[7] + "_|_" + place[8] + "_")
    print("_" + place[3] + "_|_" + place[4] + "_|_" + place[5] + "_")
    print(" " + place[0] + " | " + place[1] + " | " + place[2] + " ")


def game():
    global place
    global a
    place = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    turn = 0
    while True:

        board()
        hMove()
        turn = turn + 1
        judge()
        cMove()
        turn = turn + 1
        judge()
game()