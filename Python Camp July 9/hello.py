
name = input("What is your name? ")

thirsty = input("Hello " + name + ", are you thirsty?")

if thirsty == "yes":
    print("Go get some water!")
elif thirsty == "no":
    print("Okay then.")
else:
    print("I do not understand you. Please answer yes or no")

hungry = input("Hello " + name + ", are you hungry?")

if hungry == "yes":
    print("Go get some food!")
elif hungry == "no":
    print("Okay then.")
else:
    print("I do not understand you. Please answer yes or no")
