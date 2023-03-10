# Ex: Hello World --> hELLO wORLD

# Create the function
def Alternate_case(text):
    result = []
    for i in text:
        if i == i.lower():
            result.append(i.upper())
        else:
            result.append(i.lower())
    print(''.join(result))

Alternate_case('HELLo World')
