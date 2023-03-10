"""

Find item in a matrix and 
sum all elements located around it (up, left, down, right)

"""

def findItem(matrix,item):

    rows = len(matrix)
    columns = len(matrix[0])
    result = []
    
    # Find the coordinates of the item first
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == item:
                item_i, item_j = i, j
    
                ### Find all neighbors
                # Find up
                if 0<= item_i - 1 <= rows - 1:
                    result.append(matrix[item_i-1][j])

                # Find left
                if 0<= item_j - 1 <= columns - 1 :
                    result.append(matrix[i][item_j-1])

                # Find down
                if 0<= item_i + 1 <= rows - 1:
                    result.append(matrix[item_i+1][j])

                # find right
                if 0<= item_j + 1 <= columns - 1:
                    result.append(matrix[i][item_j+1])

    returb sum(result)

mat = [[1,2,3],
        [4,5,6],
        [7,8,9]]
        
findItem(mat,5)
