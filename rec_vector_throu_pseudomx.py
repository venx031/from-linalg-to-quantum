#rec_vector_throu_pseudomx.py

import numpy as np

#preparing
u = np.array([1, 0])
v = np.array([0, 1])
psi = np.kron(u, v)

P = np.outer(psi, np.conj(psi))
I = np.eye(4)
M = P + 0.1 * I

y = M @ psi

#decomposition and inversion
M_inv = np.linalg.pinv(M)

#projection
psi_rec = M_inv @ y

#check
check = np.allclose(psi, psi_rec)
similarity = np.dot(psi, psi_rec)

print(check) # answer: True
print(similarity) # answer: 1.0