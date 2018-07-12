from random import randint



def three_letter_words()
    alpha = ["A", 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    words = []


    x = 1
    while x < 17576:
        random = randint(0,25)
        a = random
        random = randint(0, 25)
        b = random
        random = randint(0, 25)
        c = random
        word = alpha[a] + alpha[b] + alpha[c]



        if word in words:
           pass
        else:
            print(word)
            words.append(word)
            x += 1



