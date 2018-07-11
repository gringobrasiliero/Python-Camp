
name = input("What is your name? ")
print("Hello, " + name)


def thirst():
    thirsty = input("Are you thirsty?")
    if thirsty == "yes":
        print("Go get some water!")
    elif thirsty == "no":
        print("Okay then.")
    else:
        print("I do not understand you...")
        thirst()
thirst()