letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letTwo = 0
letOne = 0


x = 1
q = 1

while w < 27:

    while x <= 26:
        for i in letters:
            print(letters[letOne] + letters[letTwo] + i)
        letTwo += 1
        x += 1
