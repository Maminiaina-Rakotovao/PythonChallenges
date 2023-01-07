# Ex: create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"


# Create the function
def Phone_number(n):
    #p1=''.join(str(n[:3]))
    string = ''.join(str(i) for i in n)
    p1 = '('+string[:3]+')'
    p2 = string[3:6]+'-'+string[6:]
    #print(p1,p2)
    print(p1+' '+p2)

Phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
