# This program will convert binary number to decimal number

# Create the main function
def main():
    # Ask the user to enter the binary number (Let's consider that the user enter a binary number for the moment)
    number = input('Enter your binary number: ')
    number = str(number)  # Convert into string facilitate the slicing method

    # Create a void list to store the sliced number
    my_list = []

    for i in number:
        my_list.append(int(i))

    # Initialize the sum 
    sum = 0
    exp = len(my_list) - 1 # -1 is used because python count from 0
    for j in my_list:
        sum = sum + j*(2**exp)
        exp = exp - 1
    
    # Display the result
    print('({})2 = ({})10'.format(number,sum))

main()
