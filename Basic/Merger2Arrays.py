def merge_arrays(arr1, arr2):
    # Create an empty set to store data
    result = set()
    for i in arr1:
        result.add(i)
    for i in arr2:
        result.add(i)
    final_result = list(result)
    final_result.sort()
    return final_result
