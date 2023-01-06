# # This program will return a tuple with 3 elements, the first, the third and the second element from the last for an given array.
# Ex:
# (6,2,9,4,3,9) --> (6,9,3)

# Create the easy_unpack function
def Easy_unpack(val):
    return (val[0],val[2],val[len(val)-2])

#Easy_unpack()
    
x = Easy_unpack([1,4,3,6,67,9,0])
print(type(x))
