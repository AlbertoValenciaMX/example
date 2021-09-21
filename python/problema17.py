import numpy as np
A = [[120, -20, 1], [-80, 80, 1], [-40, -60, 120]]
B = [[400],[0], [200]]
x = np.dot(np.linalg.inv(A), B)
print("Las concentraciones son:")
print("C1= "+ str(x[0]))
print("C2= "+ str(x[1]))
print("C3= "+ str(x[2]))