def matrix_addition(a, b):
    """"
    Visualization:

    |1 2 3|     |2 2 1|     |1+2 2+2 3+1|     |3 4 4|
    |3 2 1|  +  |3 2 3|  =  |3+3 2+2 1+3|  =  |6 4 4|
    |1 1 1|     |1 1 3|     |1+1 1+1 1+3|     |2 2 4|


    """
    rows = len(a)
    columns = len(a[0])

    sum = [[0]* rows for i in range(columns)]

    for j in range(columns):
        for i in range(rows):
            sum[i][j] = a[i][j] + b[i][j]
            
    return sum