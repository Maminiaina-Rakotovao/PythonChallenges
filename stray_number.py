def stray_number(array):
	unique = [unique_number for unique_number in array if array.count(unique_number)==1]
	print(unique)

stray_number([17, 17, 3, 17, 17, 17, 17])
