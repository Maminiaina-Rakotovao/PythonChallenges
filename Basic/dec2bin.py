# The program will convert any decimal number to binary numbers

# Create the main function
def main():
    # Ask the user to enter the number
    number = input('Enter the decimal number you want to convert: ')
    number = int(number)

    # Create a list to store the data
    rest = []
    div = [number]

    while div[len(div)-1] != 1:
        for i in div:
            d = int(i/2)
            r = i%2
        div.append(d)               # Used to verify the while condition
        rest.append(str(r))

    rest.append('1')                
    rest.reverse()                  # Using the reverse method proposed by default in python

    result = ''.join(rest)

    print('({})10 = ({})2'.format(number,result))

# Call the main function
main()
