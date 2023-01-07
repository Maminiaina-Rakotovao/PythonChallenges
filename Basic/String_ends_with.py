# Ex: solution('abc', 'bc') # returns true
# Ex: solution('abc', 'd') # returns false

# Create the function
def String_ends_with(string,ending):

    print(string[len(string)-len(ending):])
    if string[len(string)-len(ending):]==ending:
        return True
    else:
        return False
