"""

Write a function that when given a number >= 0, returns an Array of ascending length subarrays.

pyramid(0) => [ ]
pyramid(1) => [ [1] ]
pyramid(2) => [ [1], [1, 1] ]
pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]

"""


def pyramid(number):
    mydict= dict()
    for i in range(1,number+1):
        mydict[i] = [1]*i
    return list(mydict.values())
