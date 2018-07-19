# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hints:
# Consider use range(#begin, #end) method

#
# sol = []
# for i in range(2000, 3200):
#     if i % 7 == 0 and i%5 != 0:
#         sol.append(i)
#
# print(sol)
###############################################################################################

# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


def factorial():
    sol = int(input("number please."))
    y = sol - 1
    while y > 0:
        sol = sol * y
        y-=1
    print(sol)

##########################################################################
# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
#
# Hints:
# Use __init__ method to construct some parameters


class Student(name):
    name = self
    def hello(self):
        print("Hello, I want to learn how to hack the main frame.")


silas = Student()

hello()


