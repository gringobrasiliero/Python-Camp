place = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def board():
    print("_" + place[6] + "_|_" + place[7] + "_|_" + place[8] + "_")
    print("_" + place[3] + "_|_" + place[4] + "_|_" + place[5] + "_")
    print("_" + place[0] + "_|_" + place[1] + "_|_" + place[2] + "_")

def h_Move():
    move = int(input("Your turn."))-1
    place[move] = "X"


def game():
    while True:
        board()
        h_Move()

game()
