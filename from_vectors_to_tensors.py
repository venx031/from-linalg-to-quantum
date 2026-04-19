#from_vectors_to_tensors.py

import numpy as np

#vectors norm
v = np.array([1+2j, 3-4j])
v_norm = v / np.linalg.norm(v)

print(v_norm)

#matrix
H = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1] ])
I = np.eye(2)
H_dag = H.conj().T
res = H_dag @ H

print(np.allclose(res, I))

#svd
A = np.random.randint(16, size=(4, 4))
U, S, V = np.linalg.svd(A)
k = 2
U_k = U[:, :k]
D_k = np.diag(S[:k])
V_k = V[:k, :]
res = U_k @ D_k @ V_k
res.shape

print(res)

#tensor mul
a = np.array([1, 0])
b = (1/np.sqrt(2)) * np.array([1, 1])
c = np.kron(a, b)

print(c)