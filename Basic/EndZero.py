# This program try to find zero at the end of a sequence


# create the end_zeros function
def end_zeros(value):
    for j in value:
        if j=='0':
            return len(value)
        else:
            i = 1
            while value[len(value)-i] == '0':
                i = i + 1
            return i-1
