# Ex: ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) => [4, 6, 8]
# Ex: ([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2) => [-8, 26]
# Ex: ([6, -25, 3, 7, 5, 5, 7, -3, 23], 1) => [6]

# Create the function
def Even_array(arr,n):
    even_list=[]
    for i in arr:
        if i%2==0:
            even_list.append(i)
        
    print(even_list[len(even_list)-n:])

Even_array([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2)
