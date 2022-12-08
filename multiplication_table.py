def multi_table(number):
    list= []
    for i in range(1,11):
        result = '{} * {} = {}\n'.format(i,number,i*number)
        list.append(result)
    final = list[-1]
    final_list=[]
    for i in final:
        final_list.append(i)
    del list[-1]
    del final_list[-1]
    list.append(''.join(final_list))
    print(list)
multi_table(5)
