from random import choice

x = ["Rock", "Paper", "Scissors"]




def rps():
    hChoice = input("Rock, Paper, or Scissors? (r,p, or s)")
    cChoice = choice(x)
    if hChoice == "r" or hChoice == "p" or hChoice == "s":
        print("Computer chose " + cChoice)

        if hChoice == "r" and cChoice == "Scissors":
            print("You win!")
        elif hChoice == "p" and cChoice == "Rock":
            print("You win!")
        elif hChoice == "s" and cChoice == "Paper":
            print("You win!")

        elif cChoice == "Rock" and hChoice == "s":
            print("You lose!")
        elif hChoice == "r" and cChoice == "Paper":
            print("You lose!")
        elif hChoice == "p" and cChoice == "Scissors":
            print("You lose!")

        else:
            print("Tie")
    else:
        print("Only r, p or s. ")

while True:
    rps()