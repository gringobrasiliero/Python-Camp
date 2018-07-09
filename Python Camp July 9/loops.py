
height = int(input("How high?"))

block = "[]"
air = "  "
num = 0

while num <= height:
    print((air * (height-num)) + block)
    block = block + "[]"
    num = num + 1
