def Filter(string):
    number = [0,1,2,3,4,5,6,7,8,9]
    
    # Replace white space in case there is in the input
    string = string.replace(" ","")
    
    my_number = [my_string_number for my_string_number in string if my_string_number in str(number)]
    return int(''.join(my_number))
