#low_rank_appro.py

import numpy as np

#create matrix
A = np.random.randint(9, size=(3, 3))
B = np.random.randint(9, size=(3, 3))
M = np.kron(A, B)

#svd
U, S, Vh = np.linalg.svd(M)
k = 1
S_red = S.copy()
S_red[:k] = 0
rec = U @ np.diag(S_red) @ Vh

print(rec) # answer:  1.04455207e+01]
#                     [-5.14432260e+00 -4.04095997e+00 -2.33232655e+00  9.67873810e-01
#                     2.61653989e-01 -1.73483784e+00  1.14716223e+01  8.01391286e+00
#                     8.53687288e-01]]
