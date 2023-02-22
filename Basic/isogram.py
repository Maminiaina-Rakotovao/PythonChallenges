"""

Description:

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false


"""


def is_isogram(string):
    #your code here
    if string == '':
        return True
    result = []
    string = string.lower()
    for i in string:
        result.append(string.count(i))
    result.sort()
    return True if result[0]==result[-1] else False
