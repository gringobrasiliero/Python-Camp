
name = input("What is your name? ")



def areYouThirsty():
    thirsty = input("Hello " + name + ", are you thirsty?")

    if thirsty == "yes":
        print("Go get some water!")
    elif thirsty == "no":
        print("Okay then.")
    else:
        print("I do not understand you. Please answer yes or no")
        areYouThirsty()

areYouThirsty()
