#lm_through_QR.py

import numpy as np
import scipy

#create_matrix and vector
M = np.random.randint(9, size = (3, 3))
v = np.array([[100, 250, 400] ])

#QR
Q, R = np.linalg.qr(M)
d = np.transpose(Q) @ v.T
beta = scipy.linalg.solve_triangular(R, d)

#pred
pred = np.dot(M, beta)
mse = np.mean((v.T - pred)**2)
print(mse)