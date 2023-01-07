#Examples (Input --> Output)

#[1,2,3,4,5] --> [1,5]
#[2334454,5] --> [5,2334454]
#[1]         --> [1,1]

def min_max(lst):
    min_lst = min(lst)
    max_lst = max(lst)

    return [min_lst,max_lst]
