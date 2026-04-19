#invariance_trace.py

import numpy as np

#invariance_trace
A = np.random.randint(9, size=(3, 3))
eigenvalues = np.linalg.eigvals(A)
check = np.allclose(np.trace(A), np.sum(eigenvalues))
check_det = np.allclose(np.linalg.det(A), np.prod(eigenvalues))

print(check) # answer: True
print(check_det) # answer: True

#create_vector_throu_tensor
a = np.array([1, 0])
b = np.array([0, 1])
psi = np.kron(a, b)
P = np.outer(psi, psi)

check_P = np.allclose(P**2, P)

print(P) # answer: [[0 0 0 0]
#                   [0 1 0 0]
#                   [0 0 0 0]
#                   [0 0 0 0]]
print(check_P) # answer: True

#rec_svd_low_appro
Mx_rand = np.random.randint(25, size=(5, 5))

U, S, Vh = np.linalg.svd(Mx_rand)
k = 2
U_k = U[:, :k]
S_k = np.diag(S[:k])
Vh_k = Vh[:k, :]
rec = U_k @ S_k @ Vh_k

err = np.linalg.norm(Mx_rand - rec)

print(rec)
print(err) # answer: 22.7604542175433