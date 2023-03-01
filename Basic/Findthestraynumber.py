"""

Examples

[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3

"""

def stray(arr):
    for i in arr:
        if arr.count(i)==1:
            return i
          
