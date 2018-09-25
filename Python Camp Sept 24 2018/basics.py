
name = input("what is your name?")



def thirst():
    thirsty = input("Hello, " + name + ", are you thirsty?")
    if thirsty == "yes":
        print("Go get some water.")
    elif thirsty == "no":
        print("okay")
    else:
        print("What?")
        thirst()
thirst()
