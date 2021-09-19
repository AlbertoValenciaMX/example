import matplotlib.pyplot as plt
import numpy as np
import math

d = 3
TenF = np.zeros(d)
TenC = np.zeros(d)
TenF[0] = 20
TenF[1] = 40
TenF[2] = 60
n = 401
TeqF = np.zeros(n)
TeqC = np.zeros(n)
VF = np.zeros(n)
VC = np.zeros(n)
VF[1] = 4
for j in range(0, d):
    TenC[j] = (TenF[j]-32) * 5 / 9
    for k in range(1, n-1):
        VC[k] = VF[k] * 1.60934
        TeqF[k] = (91.4 - (91.4 - TenF[j])) * (0.0475 -
                                               0.0203 * VF[k] + 0.304 * math.sqrt(VF[k]))
        TeqC[k] = ((91.4 - 32) * 5 / 9 - ((91.4 - 32) * 5 / 9 - TenC[j])) * (0.0475 * 1.60934 - 0.0203 * VC[k] +
                                                                             0.304 * math.sqrt(VC[k])) * 9 / 5 + 32
        VF[k + 1] = VF[k] + 0.1
    plt.figure("En unidades originales problema ")
    plt.scatter(TeqF, VF)
    plt.xlabel("T equivalente en ºF")
    plt.ylabel("Velocidad del aire en millas/h")
    plt.figure("En unidades SI")
    plt.scatter(TeqC, VC)
    plt.xlabel("T equivalente en ºC")
    plt.ylabel("Velocidad del aire en km/h")

plt.show()
