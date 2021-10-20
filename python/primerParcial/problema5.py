import matplotlib.pyplot as plt
import numpy as np

P1 = 7
T = 600
Vel = 60
A1 = 0.015
P2 = 25
A2 = 0.14
x2 = 0.95
Qs = 20
Voles = 0.055820432
DenEntr = 17.91458731
h1 = 3650.03606
m1 = Vel * DenEntr * A1
print("El valor del flujo masico del vapor en kg/s es: ", m1)
Tsat = 64.8239
vf = 0.001019822
vg = 6.312686533
hf = 271.1588605
hg = 2616.609112
v2 = ((1 - x2) * vf) + (x2 * (vg))
DenSal = v2**-1
Vel2 = m1 / (DenSal * A2)
print("El valor de la velocidad de salida en m/s es: ", Vel2)
h2 = ((1 - x2) * hf) + (x2 * (hg))
Ws = (m1 * h1) + (m1 * ((Vel**2) / (1000 * 2))) - \
    (m1 * h2) - (m1 * ((Vel2**2) / (1000 * 2))) - (Qs * m1)
print("El valor de la potencia desarrollada de salida en KW es:", Ws)
Pressu = np.array([10, 15, 20, 25, 30, 40, 50])
vft = np.array([0.001010, 0.001014, 0.001017, 0.001020, 0.001022, 0.001026, 0.001030])
vgt = np.array([14.670, 10.020, 7.6481, 6.2034, 5.2287, 3.9933, 3.2403])
hft = np.array([191.81, 225.94, 251.42, 271.96, 289.27, 317.62, 340.54])
hgt = np.array([2583.9, 2598.3, 2608.9, 2617.5, 2624.6, 2636.1, 2645.2])
n = 7
v = np.zeros((0, n))
D = np.zeros((1, n))
vel = np.zeros((1, n))
for i in range(1, n):
    A = 0.1
    v[0, i] = (np.dot((1 - x2), vft[i])) + (np.dot(x2, (vgt[i])))
    D[1, i] = v[1, i]**-1
    vel[1, i] = m1 / (A * D[1, i])
print(v)
print(D)
print(vel)
h = np.zeros((1, n))
W = np.zeros((1, n))
for i in range(0, n):
    h[1, i] = ((1 - x2) * hft[i]) + (x2 * (hgt[i]))
    W[1, i] = (m1 * h1) + (m1 * ((Vel**2) / (1000 * 2))) - \
        (m1 * h[1, i]) - (m1 * ((vel[1, i]**2) / (1000 * 2))) - (Qs * m1)
print(W)
plt.figure(1)
plt.plot(Pressu, vel)
plt.grid("on")
plt.scatter(Pressu, vel)
plt.xlabel("Presion de salida (kPA)")
plt.ylabel("Velocidad de salida (m/s)")

plt.show()
