# This program will determine which digit in the given number is the biggest
# Ex: input --> output
# 1 --> 1
# 251 --> 5
# 74 --> 7

# Create a list to store variable
digit_list = []

# Create the maxdigit function
def Max_digit(number):
    for i in number:
        digit_list.append(int(i))
    retrun max(digit_list)

