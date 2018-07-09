

name = input("What is your name?")

print("Hello " + name)



def areYouThirsty():
    thirsty = input( name + ", are you thirsty?")

    if thirsty == "yes":
        print("Go get some water.")
    elif thirsty == "no":
        print("Okay then")
    else:
        print("What?")
        areYouThirsty()

areYouThirsty()


