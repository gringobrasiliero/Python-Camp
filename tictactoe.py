from random import randint

place = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

win_combo = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [6,4,2], [0,4,8]]

def win():
    for i in win_combo:
        if place[i[0]] == place[i[1]] == place[i[2]] == "X":
            print( "Human Wins!")
            game()
            again()
        elif place[i[0]] == place[i[1]] == place[i[2]] == "X":
            print("CPU Wins!")
            game()
            again()
def again():
    rematch = input("Would you like to play again? (y or n) ")
    if rematch == "y":
        game()
    elif rematch == "n":
        exit()
    else:
        print("What?")
        again()
# def win():

def human_move():
    move = int(input("Put an X in one of the spots"))-1
    if place[move] == "X" or place[move] == "O":
        print("Somebody went there already, try again.")
        human_move()
    else:
        place[move] = "X"

def cpu_move():
    cpuMove = randint(0,8)
    if place[cpuMove] == "X" or place[cpuMove] == "O":
        cpu_move()
    else:
        place[cpuMove] = "0"

def board():
    print("_" + place[6] + "_|_" + place[7] + "_|_" + place[8] + "_")
    print("_" + place[3] + "_|_" + place[4] + "_|_" + place[5] + "_")
    print(" " + place[0] + " | " + place[1] + " | " + place[2] + " ")


def game():

    while True:
        board()
        human_move()
        cpu_move()
# game()