from random import randint
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# for k in letters:
#     for j in letters:
#         for i in letters:
#             print(i + j + k)


def randomLetters():
    words = []
    while x < 17576:
        a = randint(0, 25)
        b = randint(0, 25)
        c = randint(0, 25)
        word = letters[a] + letters[b] + letters[c]
        if word not in words:
            print(word)
            words.append(word)
            x += 1

# randomLetters()


