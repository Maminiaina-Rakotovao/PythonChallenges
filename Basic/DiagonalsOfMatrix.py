"""
Create a function that calculates all possible diagonals of a given (square) matrix. Diagonals must be laid out from top to bottom

    Matrix = array of n length whose elements are n length arrays of integers.

2x2 example:

diagonals( [
  [ 1, 2 ],
  [ 3, 4 ]
] ); 

returns -> [ [ 1 ], [ 2, 3 ], [ 4 ], [ 2 ], [ 1, 4 ], [ 3 ] ]

it is valid too -> [ [ 1, 4 ], [ 3 ], [ 2 ], [ 2 , 3 ], [ 1 ], [ 4 ] ] //Order of the returned array does not matter

it is invalid -> [ [ 1 ], [ 3, 2 ], [ 4 ], [ 2 ], [ 1, 4 ], [ 3 ] ] //Order of each diagonal must be preserved

3x3 example:

diagonals( [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
] ); 

returns ->

[ [ 1 ],
  [ 2, 4 ],
  [ 3, 5, 7 ],
  [ 6, 8 ],
  [ 9 ],
  [ 3 ],
  [ 2, 6 ],
  [ 1, 5, 9 ],
  [ 4, 8 ],
  [ 7 ] ]

The tests verify that the implementation is efficient (1000x1000 matrix are used in tests).

"""

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
    return l_result+r_result

