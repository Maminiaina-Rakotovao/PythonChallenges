# This program will square every digit of a number and concatenate them
# Ex: 9119 --> 811181 

# Create the function
def Square_digit(num):
    result=[]
    for i in str(num):
        s = int(i)**2
        result.append(str(s))
    return ''.join(result)
