# The first element of a given list should become the last one
# input --> output
# [1,9,'c',4] --> [9,'c',4,1]
# [1] --> [1]
# [] --> =[]

# Create the replacefirst function
def Replace_first(mylist: list):
    if mylist == []:
        print([])
    else:
        # get the first item in the list
        first_item = mylist[0]

        # append the first_item
        mylist.append(first_item)

        # Now, delete the first element
        del mylist[0]
        return mylist

