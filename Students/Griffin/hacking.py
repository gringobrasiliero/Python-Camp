from random import randint
letters = ["A", 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
words=[]

x = 1
while x < 17576:


    a = letters[randint(0,25)]
    b = letters[randint(0,25)]
    c = letters[randint(0,25)]
    word = (a + b + c)

    if word in words:
        pass
    else:
        words.append(word)
        x += 1
        print(word)




