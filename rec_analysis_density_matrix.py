#rec_analysis_density_matrix.py

import numpy as np

#preparing
u = np.array([1, 0])
v = np.array([0, 1])
psi = np.kron(u, v)

#matrix
P = np.outer(psi, np.conj(psi))
I = np.eye(4)
M = P + 0.1 * I

#svd
U, S, Vh = np.linalg.svd(M)

#check
M_tr = np.trace(M)
check = np.allclose(M_tr, np.sum(S))

print(check) # answer: True
print(S) # answer: [1.1 0.1 0.1 0.1]