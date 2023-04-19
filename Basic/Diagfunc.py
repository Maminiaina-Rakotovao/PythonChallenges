def diagonals(matrix):
    if len(matrix)==0:
        return []
    # Diagonal to the left
    l=[(0,i) for i in range(len(matrix[0]),-len(matrix)-1,-1)]
    l_list=[]
    for i, j in l:
        l_list1 = []
        for k in range(len(matrix)):
            l_list1.append((i,j))
            i+=1
            j+=1
        l_list.append(l_list1[:])
    
    # Diagonal to the right
    r=[(0,i) for i in range(len(matrix[0])+len(matrix))]
    r_list = []
    for i, j in r:
        r_list1 = []
        for k in range(len(matrix)):
            r_list1.append((i,j))
            i+=1
            j-=1
        r_list.append(r_list1[:])
       
    l_result = []
    for k in l_list:
        l_result1=[]
        for i,j in k:
            if 0 <= j <= len(matrix[0])-1 and 0 <= i <= len(matrix):
                l_result1.append(matrix[i][j])
        l_result.append(l_result1[:])
        
	
    r_result = []
    for k in r_list:
        r_result1 = []
        for i,j in k:
            if 0 <= j <= len(matrix[0])-1 and 0 <= i <= len(matrix):
                r_result1.append(matrix[i][j])
        r_result.append(r_result1[:])	
		
    for i in l_result:
        if len(i)==0:
            l_result.remove(i)
	
    for i in r_result:
        if len(i)==0:
            r_result.remove(i)
    if l_result == r_result:
        return l_result

    l_Result = []
    for i in l_result:
        l_prod = 1
        for j in i:
            l_prod = l_prod*j
        l_Result.append(l_prod)
    
    r_Result = []
    for i in r_result:
        r_prod = 1
        for j in i:
            r_prod = r_prod*j
        r_Result.append(r_prod)
    print(sum(l_Result) - sum(r_Result))

mat = [[1,2,3,4,5,6],
        [7,8,9,10,11,12],
        [13,14,15,16,17,18],
        [19,20,21,22,23,24],
        [25,26,27,28,29,30]]

diagonals(mat)



"""
****Solution

def diagonals(matrix):
    if len(matrix) == 1: return matrix
    
    ds = []

    for y in range(0, len(matrix)):
        ds.append([matrix[y + s][s] for s in range(0, len(matrix) - y)])
        ds.append([matrix[y + s][len(matrix) - s - 1] for s in range(0, len(matrix) - y)])

    for x in range(1, len(matrix)):
        ds.append([matrix[s][x + s] for s in range(0, len(matrix) - x)])
        ds.append([matrix[s][len(matrix) - x - s - 1] for s in range(0, len(matrix) - x)])

    return ds



"""
