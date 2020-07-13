import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

A = np.array([[3, 2], [5, 2]])
w, v = la.eig(A)
print(w)
print(v)
# plt.figure(figsize=(9.5, 9.5))
# plt.quiver(0, 0, A[0][0], A[0][1], scale=1, units='xy', color='r')
# plt.quiver(0, 0, A[1][0], A[1][1], scale=1, units='xy', color='r')


plt.quiver(0, 0, v[:, 0][0], v[:, 0][1], scale=1, units='xy', color='r')
plt.quiver(0, 0, v[:, 1][0], v[:, 1][1], scale=1, units='xy', color='r')

B = np.array([v[:, 0]*w[0], v[:, 1]*w[1]])
print(B[0][0], B[0][1])
plt.quiver(0, 0, B[0][0], B[0][1], scale=1, units='xy', color='b')
plt.quiver(0, 0, B[1][0], B[1][1], scale=1, units='xy', color='b')
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.grid(axis="both")
    ``plt.show()