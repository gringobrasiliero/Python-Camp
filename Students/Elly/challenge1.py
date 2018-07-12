alpha = ["A", 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
words = []
word = alpha[0] + alpha[0] + alpha[0]


# print(word)
#
# words.append(word)
while a < 25:

    while b < 25:

        for i in alpha:
            print( alpha[a] + alpha[b] + i)

b += 1
if b == 25:
    a += 1
