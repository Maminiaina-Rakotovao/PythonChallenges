def pyramid(number):
    mydict= dict()
    for i in range(1,number+1):
        mydict[i] = [1]*i
    return list(mydict.values())
