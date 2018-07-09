
x = 1

height = int(input("How high do you want the pyramid? "))
block = "[]"
air = "  "

while x <= height:
    print((air*(height-x)) + block)
    x += 1
    block += "[]"

