#LA_baseQR.py
import numpy as np
import scipy

#matrix
A = np.random.randint(9, size=(3, 3))
b = np.array([23, 50, 44])
Q, R = np.linalg.qr(A)
d = np.transpose(Q) @ b
bs = scipy.linalg.solve_triangular(R, d)

#check
check = np.dot(A, bs)

print(check)