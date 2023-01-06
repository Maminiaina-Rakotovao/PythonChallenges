# Display the Fibonaci suit

# Create the main function
def main():
    # Create the initial suit 
    l = [0,1]

    # ask the user to enter the length of the suit
    n = input('Enter the length of the suit you want: ')
    n = int(n)
    j = 1    # loop condition
    while j <= n:
        i = len(l)
        s = l[i-1] + l[i-2]
        l.append(s)
        j = j + 1

    # Display the result
    print(l[:n])

# Call the main function
main()
