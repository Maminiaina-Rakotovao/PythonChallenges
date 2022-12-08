# This program will determine the most frequently occuring string in a given sequence.



# Create the function
def Most_frequent(text):
    # Create list to store data
    result = []

    for i in text:
        result.append(text.count(i))

    # Get the index the max in the result
    index_max = result.index(max(result))
    
    print(text[index_max])

Most_frequent(['a','b','c','b'])

