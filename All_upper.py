# This program return True if all symbols in a given string are upper case and False anyway.

# Create the allupper function
def all_upper(text):
    if text == text.upper():
        print('True')
    else:
        print('False')

# Call the function
        
t = input('Enter: ')
all_upper(t)