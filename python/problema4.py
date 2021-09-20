import numpy as np

y = [1.787e-3, 1.519e-3, 1.307e-3, 1.002e-3,
     7.975e-4, 6.529e-4, 4.665e-4, 3.547e-4, 2.828e-4]
x = [273.15, 278.15, 283.15, 293.15, 303.15, 313.15, 333.15, 353.15, 373.15]
m = 4
n = 9
xi = 0
yi = 0
xi2 = 0
xi3 = 0
xi4 = 0
xi5 = 0
xi6 = 0
xi7 = 0
xi8 = 0
xiyi = 0
xi2yi = 0
xi3yi = 0
xi4yi = 0
a0 = a1 = a2 = a3 = a4 = 1
for i in range(0, n):
    xi = xi + (x[i])
    yi = yi + (y[i])
    xi2 = xi2 + (x[i] ** 2)
    xi3 = xi3 + (x[i] ** 3)
    xi4 = xi4 + (x[i] ** 4)
    xi5 = xi5 + (x[i] ** 5)
    xi6 = xi6 + (x[i] ** 6)
    xi7 = xi7 + (x[i] ** 7)
    xi8 = xi8 + (x[i] ** 8)
    xiyi = xiyi + (x[i] * y[i])
    xi2yi = xi2yi + ((x[i] ** 2) * y[i])
    xi3yi = xi3yi + ((x[i] ** 3) * y[i])
    xi4yi = xi4yi + ((x[i] ** 4) * y[i])

E = [[n, xi, xi2, xi3, xi4], [xi, xi2, xi3, xi4, xi5], [xi2, xi3, xi4,
                                                        xi5, xi6], [xi3, xi4, xi5, xi6, xi7], [xi4, xi5, xi6, xi7, xi8]]
M = [[yi], [xiyi], [xi2yi], [xi3yi], [xi4yi]]

z = np.dot(np.linalg.inv(E), M)
A = 0.4892920416314155
B = -0.0056890474184001505
C = 2.4915226980226635e-5
D = -4.861560886151861e-8
E = 3.56198345152119e-11
print("Valores de las constantes de la relación desarrollada ")
print(z)
print("Valor de A: ", A)
print("Valor de B: ", B)
print("Valor de C: ", C)
print("Valor de D: ", D)
print("Valor de E: ", E)
