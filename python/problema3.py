import matplotlib.pyplot as plt
import numpy as np
import math

miu = 0.38
D = 0.3  # m
w1 = 1450  # en rpm
w2 = 1398  # en rpm
w = 2 * math.pi * abs(w1 - w2) / 60  # Velocidad angular relativa
ls = 10
s = 0.1 / 1000
a = ls / s
h = np.zeros(100)
T = np.zeros(100)
for i in range(0, 99):
    h[i + 1] = h[i] + s
    T[i + 1] = math.pi * miu * w * (D**4) / (32 * h[i + 1])
h[0] = 0.000099
T[0] = math.pi * miu * w * (D**4) / (32 * h[1])

plt.figure(1)
plt.scatter(h, T, color="pink", label="")
plt.plot(h, T)
plt.grid("on")

print(" h = ", h[31], " T = ", T[31])  # valor medio
plt.show()
