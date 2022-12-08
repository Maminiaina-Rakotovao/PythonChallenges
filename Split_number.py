#This program will split into pairs of the two characters a given string.

# Create the function
def split_pairs(text):
    # Create an empty list to store the result
    result =[]
    if len(text)%2 == 0:
        j = 0
        for i in range(2,len(text)+1,2):
            result.append(text[j:i])
            j = j + 2
    else:
        text = text+'_'
        j = 0
        for i in range(2,len(text)+1,2):
            result.append(text[j:i])
            j = j + 2
    print(result)

split_pairs('boiwdrfou')