#projection_quantum_dimension.py

import numpy as np

#preparing vector
v = np.random.rand(2)
v_norm = np.linalg.norm(v)

#matrix
b = np.array([1, 0])
P = np.outer(b, b.conj())

#transform
psi = v / v_norm
psi_meas = P @ v

#prob
P_rob = psi.conj().T  @ P @ psi

print(P_rob) # answer: 0.9719745352690817