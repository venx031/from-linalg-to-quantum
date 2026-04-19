#partial_trace_reshape.py

import numpy as np

u = np.array([1, 0])
v = np.array([0, 1])
psi = np.kron(u, v)

P = np.outer(psi, np.conj(psi))

T = P.reshape(2, 2, 2, 2)

rho_A = np.einsum('ijkj->ik', T)

print(rho_A) # answer: [[1 0] [0 0]]