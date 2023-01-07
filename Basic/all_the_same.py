# In this mission you should check if all elements in the given list are equal.

# Input: List.

# Output: Bool.

#Example:
#assert all_the_same([1, 1, 1]) == True
#assert all_the_same([1, 2, 1]) == False
#assert all_the_same([1, 1, 1, 2]) == False
#assert all_the_same([2, 1, 1, 1]) == False


def all_the_same(elements) -> bool:
    if elements==[]:
        return True
    new_elements = [elements[0]]*len(elements)
    if new_elements == elements:
        return True
    else:
        return False
