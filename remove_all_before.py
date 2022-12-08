# This program will remove from the list all items before the given one.
# Ex: input --> output
# [[1,2,3,4,5,6],3] --> [3,4,5,6]   (remove all items before 3)
# [[1,2,3,4,5,6],5] --> [5,6]   (remove all items before 5)


# Create the function
def Removeall_before(items,border):
	if border not in items:
		return items
	else:
		get_index_item = items.index(border)
		for i in range(get_index_item):
			del items[0];
		return items

x = Removeall_before([1,2,3,5,6,2,4,90,'g'],2)
print(x)

