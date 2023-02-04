def find_unique(arr):
    arr.sort()
    print(arr)

    if(arr[0] < arr[len(arr)-1] and arr[0] < arr[len(arr)-2]):
        n = arr[0]
    else:
        n = arr[len(arr)-1]
        
	return n
	
