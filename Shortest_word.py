# Ex:
# "bitcoin take over the world maybe who knows perhaps" --> 3
# "i want to travel the world writing code one day" --> 1

# Create the shortest function
def shortest_word(s):
    my_list = []
    s_list = s.split()
    for i in s_list:
        my_list.append(len(i))
    print(min(my_list))

shortest_word("bitcoin take over the world maybe who knows perhaps")

# correction
# def find_short(s):
#     return min(len(x) for x in s.split())
