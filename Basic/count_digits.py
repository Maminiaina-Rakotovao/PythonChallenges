#You need to count the number of digits in a given string.

#Input: String.

#Output: Integer.

#Examples:
#assert count_digits("hi") == 0
#assert count_digits("who is 1st here") == 1
#assert count_digits("my numbers is 2") == 1
#assert (
#    count_digits(
#        "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
#    )
#    == 8
#)


def count_digit(string):
    number = [0,1,2,3,4,5,6,7,8,9]
    my_number = [my_string_number for my_string_number in string.replace(' ','') if my_string_number in str(number)]
    
    return len(''.join(my_number))
