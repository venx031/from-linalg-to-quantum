#spectrum_analysis.py

import numpy as np

#matrix with tensors dot
Z = np.array([[1, 0], [0, -1] ])
I = np.eye(2)
H = np.kron(Z, I) + np.kron(I, Z)

#eigenvalues
eigenvalues, eigenvectors = np.linalg.eig(H)

#check
ivl = np.argmin(eigenvalues)
min_v = eigenvectors[:, ivl]

print(ivl) # answer: 3
print(min_v) # answer: [0. 0. 0. 1.]