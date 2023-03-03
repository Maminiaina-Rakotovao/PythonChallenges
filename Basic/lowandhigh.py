"""


Examples

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"


"""


# create the function
def lowandhigh(string):

    # We are going to remove the white space in the string
    nospacestring = string.split()

    # Put each element in a list
    list = []       # empty list
    for i in nospacestring:
        list.append(int(i))

    # print the result
    return str(max(list))+' '+str(min(list))
    
