# this program try to find the number of zero at the beginning of a number



# Create the function beginzero
def begin_zero(value):
    if value[0] !='0':
        print(0)
    else:
        i = 0
        while value[i] == '0':
            i = i + 1
            if i == len(value):
                break
        return i
