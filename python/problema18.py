import numpy as np
C1 = np.zeros((5, 5))
C1r = np.array([[1],[0],[0],[0],[0]])
C1[0] = 1
V = np.array([25, 75, 100, 25])
k = np.array([0.05, 0.1, 0.5, 0.1])
Ref = np.array([0, 0, 5, 3, 0])
# balance
E = np.array([[1, 0, 0, 0, 0], [-1, 1, 0, 0, 0], [0, -1, 1, 0, 0], [0, 0, -1, 1, 0], [0, 0, 0, -1, 1]])
R = np.array([[10], [0], [5], [-2], [-3]])
Q = np.dot(np.linalg.inv(E), R)
# balance reactores
for i in range(0,4):
    C1[i + 1,i] = Q[i] - Ref[i] - np.dot(k[i], V[i])
    C1[i + 1,i + 1] = Ref[i + 1] - Q[i + 1]
C1s = np.dot(np.linalg.inv(C1), C1r)
# No se pueden tener concentraciones negativas
for i in range(0,5):
    if C1s[i] < 0:
        C1s[i] = 0
print("Las corrientes del sistema son " + str(Q))
print("Las concentraciones de A en el reactor son " + str(C1s))