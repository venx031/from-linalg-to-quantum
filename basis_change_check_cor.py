#basis_change_check_cor.py

import numpy as np

psi = np.array([1, 0, 0, 1]) / np.sqrt(2)
H = (1 / np.sqrt(2) * np.array([[1, 1], [1, -1]]))
U_total = np.kron(H, H)

#transofrm state
psi_vec = U_total @ psi

#density matrix
P = np.outer(psi, np.conj(psi))

#decompression qr
Q, R = np.linalg.qr(P)
t = np.trace(P)
I = np.eye(4)
unit = np.allclose(Q.conj().T @ Q, I)

print(Q) # answer: [[-0.70710678  0.          0.         -0.70710678]
#                   [-0.          1.          0.          0.        ]
#                   [-0.         -0.          1.          0.        ]
#                   [-0.70710678 -0.         -0.          0.70710678]]

print(unit) # answer: True
print(t) # answer: -0.7071067811865474
print(U_total) # answer: [[ 0.5  0.5  0.5  0.5]
#                        [ 0.5 -0.5  0.5 -0.5]
#                        [ 0.5  0.5 -0.5 -0.5]
#                        [ 0.5 -0.5 -0.5  0.5]]

print(psi_vec) # answer: [0.70710678 0.         0.         0.70710678]