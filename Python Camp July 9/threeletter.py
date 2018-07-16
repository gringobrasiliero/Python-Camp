

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
words = []


x = 0
y = 0
b = 0
while y <= 25:
    while x <= 25:

        for i in alpha:
            print(alpha[b] + alpha[x] + i)
        b += 1
        x += 1
    y += 1


