#svd_compress.py

import numpy as np

#create_matrix
X = np.random.randint(15, size=(5, 3))

#svd
U, S, Vt = np.linalg.svd(X)
k = 3
U_k = U[:, :k]
D_k = np.diag(S[:k])
V_k = Vt[:k, :]
rec = U_k @ D_k @ V_k

#check_ortho_matrix
I = np.eye(5)
ortho = np.isclose(U.T @ U, I)

#loss
loss = np.mean((X - rec)**2)

#print
print(rec)
print(ortho)
print(loss)