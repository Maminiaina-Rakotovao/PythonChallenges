def merge_arrays(arr1, arr2):
    # Create an empty set to store data
    result = set()
    for i in arr1:
        result.add(i)
    for i in arr2:
        result.add(i)
    final_result = list(result)
    final_result.sort()
    print(final_result,type(final_result))

merge_arrays([1, 3, -5, 7, 9, 11, 12],[1, 2, 3, 4, 5, 10, 12])
