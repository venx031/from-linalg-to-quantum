#quantum_compress_rec_channel.py

import numpy as np

#preparing (tensors mul)
a = (np.cos(3.14 / 8), np.sin(3.14 / 8))
b = np.array([1, 0])
psi = np.kron(a, b)

#transformation (matrixes)
CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0] ])
phi = CNOT @ psi

#svd
M = np.reshape(phi, (2, 2))
U, S, Vh = np.linalg.svd(M)
k = 1
U_k = U[:, 0:k]
S_comp = np.diag([S[0], 0])
Vh_k = Vh[0:k, :]
res = S[0] * (U_k @ Vh_k)

#return matrix to vector
phi_new = res.flatten()

print(phi_new)
