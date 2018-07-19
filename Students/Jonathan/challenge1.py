from random import randint
letters = "ABCDEFGHIJKLMNOPKRSTUVWXYZ"
words = []

# for x in letters:
#     for j in letters:
#         for i in letters:
#             word = x + j + i
#             print(word)
#             words.append(word)
#
# print(words.count("AAA"))









def three_letters():
    x = 1
    while x < 13824:
        a = randint(0,23)
        b = randint(0,23)
        c = randint(0,23)

        word = letters[a] + letters[b] + letters[c]
        if word in words:
            pass
        else:
            words.append(word)
            print(word)
            print("Words: " + str(x))
            print(words.count(word))
            x += 1


three_letters()