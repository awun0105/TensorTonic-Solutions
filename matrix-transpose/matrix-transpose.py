import numpy as np

def matrix_transpose(A):
    A_np = np.array(A)
    
    n, m = A_np.shape 
    
    new_array = np.zeros((m, n))
    
    for i in range(n):
        for j in range(m):
            new_array[j, i] = A_np[i, j]
    #A is a list
    #n = len(A)
    #m = len(A[0]) if n > 0 else 0
    
    #new_array = np.zeros((m, n))
    
    #for i in range(n):
      #  for j in range(m):
      #      new_array[j, i] = A[i][j]         
    return new_array

            