# This program will create a function with two arguments that will return an array of the first (n) multiple of x.
# Examples:
# count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
# count_by(2,5) #should return [2,4,6,8,10]


# Create the count_by function
def count_by(x,n):
    list = [x]
    i = 0
    while len(list) != n:
        list.append(list[i]+x)
        i = i + 1
    print(list)
count_by(5,9)
