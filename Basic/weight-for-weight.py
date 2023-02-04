def order_weight(strng):

    if strng == '':
        return ''
    else:
        # Transform strng to list
        strng_tolist = sorted(strng.split())
        result = sorted(strng_tolist, key=summ)
        return ' '.join(result)


# Calcul the sum of digit

def summ(x):
    sum = 0
    for number in x:
        for digit in number:
            sum = sum + int(digit)
    return sum
