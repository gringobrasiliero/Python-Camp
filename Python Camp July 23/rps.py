from random import randint
cmove = ""
move= ""

def hChoice():
    move = input("Rock, Paper, or Scissors (r,p,s")
    if move == "r":
        move = "Rock"
    elif move == "p":
        move = "Paper"
    elif move == "s":
        move = "Scissors"
    else:
        print("Use r, p, or s.")
        hChoice()
    return move

def cChoice():
    cmove = randint(1,3)
    if cmove == 1:
        cmove = "Rock"
    elif cmove == 2:
        cmove = "Paper"
    elif cmove == 3:
        cmove = "Scissors"
    return cmove

def judge(move, cmove):
    if move == "Rock" and cmove == "Scissors":
        print("Human Wins!")
    elif move == "Paper" and cmove == "Rock":
        print("Human Wins!")
    elif move == "Scissors" and cmove == "Paper":
        print("Human Wins!")
    elif cmove == "Rock" and move == "Scissors":
        print("CPU Wins!")
    elif cmove == "Paper" and move == "Rock":
        print("CPU Wins!")
    elif cmove == "Scissors" and move == "Paper":
        print("CPU Wins!")
    else:
        print("Tie!")

def versus(move, cmove):
    print("Human: " + move + " CPU: " + cmove)

def game():

    while True:
        move = hChoice()
        cmove = cChoice()
        versus(move, cmove)
        judge(move, cmove)

game()













