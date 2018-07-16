
# Pseudo Code
# get the marker
# stand up
# walk over to the board
# take off the cap of the marker
# place tip of marker against the board
# draw a horizontal line from left to right
# rotate  the marker 90 degrees R
# draw a vertical line (Go forward)
# turn marker 90 degrees R
# draw another horizontal line from R to L
# turn marker 90 degrees R
# draw a vertical line (Go Forward)
# remove marker off of board
# put the cap on marker tip
# step away from board
# put marker down on table.















name = input("What is your name?")


def convo():
    thirsty = input("Hello " + name + ", are you thirsty? ")

    if thirsty == "y":
        print("Go get some water.")
    elif thirsty == "no":
        print("Okay then. ")
    else:
        print("What?!?!!?")
        convo()

convo()













