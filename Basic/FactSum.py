def sum_factorial(lst):
    result = []
    for i in lst:
        fact = 1
        for num in range(1,i+1):
            fact = fact * num
        result.append(fact)
    return sum(result)