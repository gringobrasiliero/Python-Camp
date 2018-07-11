from random import choice

def human_move():
    global human
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
    return human

def cpu_move():
    global cpu
    x = ["Paper", "Rock", "Scissors"]
    cpu = choice(x)
    print(cpu)
    return cpu

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
        print("CPU Wins")
    elif cpu == "Rock" and human == "Scissors":
        print("CPU Wins")
    elif cpu == "Paper" and human == "Rock":
        print("CPU Wins")


def game():

    while True:
        human_move()
        cpu_move()
        print("Human: " + str(human) + " VS " + "CPU: " + str(cpu))
        judge()


game()