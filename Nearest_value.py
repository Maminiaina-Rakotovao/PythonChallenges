def Nearest_value(my_set:set ,x:int):
    # Transform the set into list
    my_set_list=list(my_set)

    my_set_list.append(x)

    my_set_list.sort()

    if my_set_list[0] == x:
        print(my_set_list[1])
    elif my_set_list[-1] == x:
        print(my_set_list[-2])
    else: 
        # Get the index of x in our list
        x_index = my_set_list.index(x)

        # Get the 2 items around x
        first_item = my_set_list[x_index-1]
        second_item = my_set_list[x_index+1]
        
        # Compute the difference between the 2 items and x
        diff_first_x = x - first_item
        diff_second_x = second_item - x

        if diff_first_x > diff_second_x:
            print(second_item)
        else:
            print(first_item)

Nearest_value({5,}, 7)

