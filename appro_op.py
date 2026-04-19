#appro_op.py

import numpy as np

#preparing
X = np.array([[0, 1], [1,0] ])
Z = np.array([[1, 0], [0, -1] ])
alpha = 0.5
betha = 1.0
H = alpha * np.kron(X, X) + betha * np.kron(Z, Z)

#decomposition
Q, R = np.linalg.qr(H)
H_det = np.linalg.det(R)

#values spectre
eigenvalues, eigenvectors = np.linalg.eigh(H)
H_tr = np.trace(H)
check = np.allclose(H_tr, np.sum(eigenvalues))

print(check) # answer: True

#projection vectors
b = (1 / np.sqrt(2) * np.array([1, 0, 0, 1])).T
d = Q.T @ b

#check
print(np.shape(d)) # answer: (4,)
print(np.shape(b)) # answer: (4,)
