#state_Entanglement.py

import numpy as np

#preparing the components
v = (1 / np.sqrt(2) * np.array([1, 1]))
psi = np.kron(v, v)

#matrix of transition
CZ = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1] ])

#operations
phi = CZ @ psi

#svd
phi_mx = np.reshape(phi, (2, 2))
U, S, Vh = np.linalg.svd(phi_mx)

print(f"Singular numbers: {S}")

#plot
import matplotlib.pyplot as plt
rho = np.outer(phi, phi)
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

_x = np.arange(4)
_y = np.arange(4)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

top = rho.ravel()
bottom = np.zeros_like(top)
width = depth = 0.5

ax.bar3d(x, y, bottom, width, depth, top, shade=True, color='skyblue')
ticks = ['|00>', '|01>', '|10>', '|11>']
ax.set_xticks(np.arange(4) + 0.25)
ax.set_xticklabels(ticks)
ax.set_yticks(np.arange(4) + 0.25)
ax.set_yticklabels(ticks)
ax.set_title("Density Matrix after CZ Gate (Entangled State)")

plt.show()