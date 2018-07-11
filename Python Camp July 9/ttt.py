from random import randint
place = [ "1", "2", "3", "4", "5", "6", "7", "8", "9"]
win_combos = [ [0,1,2], [3,4,5], [6,7,8], [6,3,0], [7,4,1], [8,5,2], [0,4,8], [6,4,2]]


def judge():
    global counter
    for i in win_combos:
        if place[i[0]] == place[i[1]] and place[i[1]] == place[i[2]]:
            print( place[i[0]] + " wins!")
            game()
    if counter == 9:
        print("Draw!")
        game()
def h_move():
    move = int(input("Where would you like to go?"))-1
    if place[move] == "X" or place[move] == "O":
        print("Place Taken. Try again. ")
        h_move()
    else:
        place[move] = "X"

def c_move():
    global working
    working = "nyancat"
    try_win()
    try_block()
    logic()

def try_win():
    for i in win_combos:
        if place[i[0]] == place[i[1]] == "O" or place[i[1]] == place[i[2]] == "O" or place[i[0]] == place[i[2]] == "O":
            for x in i:
                if place[x] != "O" and place[x] != "X":
                    place[x] = "O"
                    board()
                    judge()

def try_block():
    global working
    for i in win_combos:
        if place[i[0]] == place[i[1]] == "X" or place[i[1]] == place[i[2]] == "X" or place[i[0]] == place[i[2]] == "X":
            for x in i:
                if place[x] != "O" and place[x] != "X":
                    place[x] = "O"
                    working = "dog"
                    break
def logic():

    cpu_placing = [ 4, 0, 2, 6, 8]
    for i in cpu_placing:
        if place[i] != "O" and place[i] != "X":
            place[i] = "O"
            working = "dog"
            break
    if working == "nyancat":
        random()

def random():
    move = randint(0,8)
    if place[move] != "X" or place[move] != "O":
        logic()
    else:
        place[move] = "O"


def board():
    print("_" + place[6] + "_|_" + place[7] + "_|_" + place[8] + "_")
    print("_" + place[3] + "_|_" + place[4] + "_|_" + place[5] + "_")
    print(" " + place[0] + " | " + place[1] + " | " + place[2] + " ")


def game():
    global counter
    global place
    counter = 0
    place = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while True:
        board()
        h_move()
        counter +=1
        judge()
        c_move()
        counter += 1
        judge()
game()