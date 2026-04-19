#Back_substitution.py

import numpy as np

#matrix with tensors dot
Z = np.array([[1, 0], [0, -1] ])
I = np.eye(2)
H = np.kron(Z, I) + np.kron(I, Z)
b = np.array([1, 0, 0, 0])

#function
def back_sub(H, b):
    m, n = H.shape
    Q = np.zeros((m, n))
    R = np.zeros((m, n))
    V = H.copy().astype(float)

#loops 1
    for i in range(n):
        R[i, i] = np.sqrt(np.sum(V[:, i]**2))
        
        if R[i, i] > 1e-10:
            Q[:, i] = V[:, i] / R[i, i]

            for j in range(i + 1, n):
                R[i, j] = Q[:, i].T @ V[:, j]
                V[:, j] = V[:, j] - R[i, j] * Q[:, i]
        else:
             Q[:, i] = 0
    
    d = Q @ b
    x = np.zeros(n)
#loops2
    for i in range(n - 1, -1, -1):
            sum_known = 0
          
            if(i < n):
                for j in range(i + 1, n):
                    sum_known += R[i, j] * x[j]

    x[i] = (d[i] - sum_known) / R[i, i]

    return x

x_res = back_sub(H, b)
print("Results is: ", x_res)