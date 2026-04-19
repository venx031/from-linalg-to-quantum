#chek_uni_basis.py

import numpy as np

#create matrix
A = np.random.randint(16, size=(4, 4))
v = np.array([1, 0])

#decompression
Q, R = np.linalg.qr(A)
I = np.eye(16)
psi = np.kron(np.conj(Q), Q)
check = np.allclose(psi @ psi.T.conj(), I)

#norm
norm = np.linalg.norm(v)
v_16 = np.zeros(16)
v_16[0] = 1
v_new = psi @ v_16
norm_check = np.allclose(np.linalg.norm(v_new), np.linalg.norm(v_16))

print(check) # answer: True
print(norm_check) # answer: True
print(norm) # answer: 1.0