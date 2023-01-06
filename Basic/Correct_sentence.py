# This program will return a correct version of an given sentenve. A correct sentence begin with capital letter and ends with a dot.


# Create a list to store the result
Correct_result = []


# Create the function
def Correct_sentence(text):
    if text[0] != text.upper():
        for i in text:
            Correct_result.append(i)
        del Correct_result[0]
        Correct_result.insert(0,text[0].upper())
    if Correct_result[-1] != '.':
        Correct_result.append('.')
    return ''.join(Correct_result)
    
Value = input('Enter you sentence: ')
x = Correct_sentence(Value)
print(x)

