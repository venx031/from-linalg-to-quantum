#purity.py

import numpy as np

psi = np.array([1, 0, 0, 1]) / np.sqrt(2)
P = np.outer(psi, np.conj(psi))
T = P.reshape(2, 2, 2, 2)
rho_A = np.einsum('ijkj->ik', T)
gamma = np.trace(rho_A @ rho_A)

print(gamma) # answer: 0.4999999999999998

#Schmidt Decomposition
v = np.random.rand(4)
norm = v / np.linalg.norm(v)
A = norm.reshape(2, 2)

U, S, Vh = np.linalg.svd(A)
check = np.isclose(np.sum(S**2), 1.0)

print(check) # answer: True

#CNOT
CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0] ])
CNOT_dag = CNOT.conj().T
I = np.eye(4)
check_U = np.allclose(CNOT @ CNOT_dag, I)

print(check_U) # answer: True

p = np.array([1, 1]) / np.sqrt(2)
m = np.array([1, -1]) / np.sqrt(2)
psi_out = np.kron(p, m)
state = CNOT @ psi_out

print(psi_out) # answer: [ 0.5 -0.5  0.5 -0.5]
print(state) # answer: [ 0.5 -0.5 -0.5  0.5]