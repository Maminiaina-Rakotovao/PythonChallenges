# This program will return the middle character of a word. If the word's lenght is odd, the program will return the middle character.
# If the word's length is even, the program will return the twi middle characters.
# Ex:
# test --> es
# testing --> t
# A --> A

# Create the function
def Get_middle(text: str):
    # get the length of the text
    get_length = len(text)
    if get_length%2 == 0:
        print(text[int(get_length/2)-1:int(get_length/2)+1])
    else:
        print(text[int(get_length/2)])

Get_middle('t')
