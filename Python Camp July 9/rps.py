from random import choice

def human_move():
    human = input("Rock, Paper, or Scissors (r,p,s)")
    if human == "p":
        human = "Paper"
    elif human == "s":
        human = "Scissors"
    elif human == "r":
        human = "r"
    else:
        print("Invalid input: Use r, p, or s")
        human_move()


def cpu_move():
    x = ["Paper", "Rock", "Scissors"]
    cpu = choice(x)


def judge():
    if human == cpu:
        print("Draw")
    elif human == "Scissors" and cpu == "Paper":
        print("Human Wins")
    elif human == "Rock" and cpu == "Scissors":
        print("Human Wins")
    elif human == "Paper" and cpu == "Rock":
        print("Human Wins")
    elif cpu == "Scissors" and human == "Paper":
        print("Human Wins")
    elif cpu == "Rock" and human == "Scissors":
        print("Human Wins")
    elif cpu == "Paper" and human == "Rock":
        print("Human Wins")
    

def game():
    human_move()
    cpu_move()

