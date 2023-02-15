def matrix_elements_sum(matrix):
    # count rows and columns
    r = len(matrix)
    c = len(matrix[0])

    # Explore the matrix and change item below 0 to x
    for j in range(c):
        for i in range(r):
            while matrix[i][j]==0 and i<r-1:
                matrix[i+1][j]='x'
                i = i+1
            else:
                continue
    
    # sum
    s = 0
    for j in range(c):
        for i in range(r):
            if str(matrix[i][j]).isnumeric():
                s = s + matrix[i][j]
            else:
                continue
    return s