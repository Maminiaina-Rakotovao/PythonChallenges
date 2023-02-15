# Ex: solution('abc', 'bc') # returns true
# Ex: solution('abc', 'd') # returns false

# Create the function
def String_ends_with(string,ending):
    return True if string[len(string)-len(ending):]==ending else False
