#analyse_QCh_Entanglement.py

import numpy as np

#vectors, probabilities and projections
psi = (1 / np.sqrt(3)) * np.array([1, 0] ) + np.sqrt(2 / 3) * np.array([0, 1] )
e2 = np.array([0, 1])
P = np.abs(np.vdot(e2, psi))**2

print(P) # answer: 0.6666666666666666

#Controlled-NOT
CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0] ])
CNOT_dag = CNOT.conj().T
check = CNOT_dag @ CNOT

print(np.allclose(check, CNOT)) # answer: False
print(np.allclose(check, np.eye(4))) # answer: True

#eigen
S = np.array([[1, 0], [0, 1j] ])
evals = np.linalg.eigvals(S)

print(evals) # answer: [1.+0.j 0.+1.j]

#tensor dot
H = np.array(1 / np.sqrt(2)) * np.array([[1, 1], [1, -1] ])
I = np.eye(2)
Op = np.kron(H, I)

print(Op.shape) # answer: (4, 4)
