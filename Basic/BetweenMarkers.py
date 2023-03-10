# This program will find a substring between an enclosed two markers

# Example: What is [apple]','[','] ==> apple

# Create the function

def Between_markers(text,marker1,marker2):
    # find the index of the marker1 and marker2
    index_marker1 = text.index(marker1)
    index_marker2 = text.index(marker2)

    #display the result
    result = text[index_marker1+1:index_marker2]
    return result
