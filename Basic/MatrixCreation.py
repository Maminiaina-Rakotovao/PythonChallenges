"""

Create an identity matrix of the specified size( >= 0).

Some examples:
(1)  =>  [[1]]

(2) => [ [1,0],
        [0,1] ]

	      [[1,0,0,0,0],
           [0,1,0,0,0],
(5) =>     [0,0,1,0,0],
           [0,0,0,1,0],
           [0,0,0,0,1]]   


"""
import numpy as np
def get_matrix(n):
    #your code here
    return np.eye(n, dtype=int).tolist()

