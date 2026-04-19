#entanglement detector throu svd.py

import numpy as np

psi = np.array([0, 1, -1, 0]) / np.sqrt(2)
A = np.reshape(psi, (2, 2))

#svd
U, S, Vh = np.linalg.svd(A)
check = np.sum(S**2)

print(S) # answer: [0.70710678 0.70710678]
print(check) # answer: 0.9999999999999998