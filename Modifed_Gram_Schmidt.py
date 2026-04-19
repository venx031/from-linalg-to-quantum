#Modifed_Gram_Schmidt.py

import numpy as np

#matrix with tensors dot
Z = np.array([[1, 0], [0, -1] ])
I = np.eye(2)
H = np.kron(Z, I) + np.kron(I, Z)

#function
def gram_schmidt(H):
    m, n = H.shape
    Q = np.zeros((m, n))
    R = np.zeros((m, n))
    V = H.copy().astype(float)

    for i in range(n):
        R[i, i] = np.sqrt(np.sum(V[:, i]**2))

        if(R[i, i] > 1e-10):
            Q[:, i] = V[:, i] / R[i, i]
        if(i < n):
            for j in range(i + 1, n):
                R[i, j] = Q[:, i].T @ V[:, j]
                V[:, j] = V[:, j] - R[i, j] * Q[:, i]

    return Q, R

Q_res, R_res = gram_schmidt(H)

print(Q_res)