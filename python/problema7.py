import matplotlib.pyplot as plt
import numpy as np
import math

p = 3
K = 0.05
xL = -0.5
xU = 0.5
fL = xL * math.sqrt((2 * p) / (2 + xL)) / (1 - xL) - K
fU = xU * math.sqrt((2 * p) / (2 + xU)) / (1 - xU) - K
er = 100
xN = 0
n = 0
while er >= 0.0001:
    xN = (xL + xU) / 2
    fN = xN * math.sqrt(2 * p / (2 + xN)) / (1 - xN) - K
    a = fN * fU
    b = fN * fL
    if fN == 0:
        continue
    if a < 0 and b > 0:
        xL = xN
        fL = xL * math.sqrt(2 * p / (2 + xL)) / (1 - xL) - K
    if a > 0 and b < 0:
        xU = xN
        fU = xU * math.sqrt(2 * p / (2 + xU)) / (1 - xU) - K
    n = n + 1
    er = abs((xU - xL))
print("la raíz exacta es ", xN)
print("La raíz aproximada es ", xN, " con un error de ", er)
print("Número de iteraciones: ", n)

xg = np.zeros(100)
f = np.zeros(100)
acum = -0.51
for i in range(0,100):
    acum = acum + 0.01
    xg[i] = acum
    f[i] = xg[i] * math.sqrt(2 * p / (2 + xg[i])) / (1 - xg[i]) - K
plt.figure(1)
plt.plot(xg,f)
plt.scatter(xN,fN)
plt.grid("on")

plt.show()