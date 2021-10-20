import numpy as np

P = np.array([0.1, 5, 10, 20, 25, 30, 40, 45, 50])
Temp = np.array([350, 400, 450])
VT350 = np.array([220, 4.1, 2.2, 1.35, 1.1, 0.9, 0.68, 0.61, 0.54])
VT400 = np.array([250, 4.7, 2.5, 1.49, 1.2, 0.99, 0.75, 0.675, 0.6])
VT450 = np.array([282.5, 5.23, 2.7, 1.55, 1.24, 1.03, 0.78, 0.7, 0.62])

Sxy = 0
Sx = 0
Sy = 0
Sy2 = 0
Sx2 = 0
Sx3 = 0
Sx4 = 0
Sx5 = 0
Sx6 = 0
Sx2y = 0
Sx3y = 0
n = 9
Bet = np.zeros(n)
for i in range(0,n):
    Bet[i] = ((VT450[i] - VT350[i]) / (Temp[2] - Temp[0])) / (VT400[i])

V = np.zeros(n)
for i in range(0,n):
    V[i] = VT400[i] * (1 - Temp[1] * Bet[i])
    Sxy = Sxy + (P[i] * V[i])
    Sx = Sx + P[i]
    Sy = Sy + V[i]
    Sy2 = Sy2 + (V[i]**2)
    Sx2 = Sx2 + (P[i]**2)
    Sx3 = Sx3 + (P[i]**3)
    Sx4 = Sx4 + (P[i]**4)
    Sx5 = Sx5 + (P[i]**5)
    Sx6 = Sx6 + (P[i]**6)
    Sx2y = Sx2y + ((P[i]**2) * V[i])
    Sx3y = Sx3y + ((P[i]**3) * V[i])

yp = Sy / n
xp = Sx / n
A = [[n, Sx, Sx2, Sx3],[Sx, Sx2, Sx3, Sx4],[Sx2, Sx3, Sx4, Sx5],[Sx3, Sx4, Sx5, Sx6]]
B = [[Sy],[Sxy],[Sx2y],[Sx3y]]
C = np.dot(np.linalg.inv(A), B)
a = P[0]
b = P[8]
N = 11
N2 = N - 1
h = (b - a) / N2
mult3 = 0
part2 = 0
fa = np.array(C[3] * (a**2) + C[2] * (a**2) + C[1] * (a) + C[0])
fb = np.array(C[3] * (b**2) + C[2] * (b**2) + C[1] * (b) + C[0])
ff = np.zeros(N2)
x = a
for i in range(0,N2):
    x = x + h
    ff[i] = np.array(C[3] * (x**3) + C[2] * (x**2) + C[1] * (x) + C[0])
    print("Iteración: ", i, ", X= ", x, ", f(x)= ", ff[i])

for i in range(1,1,N2):
    if i % 3 == 0:
        mult3 = mult3 + ff[i]
    else:
        part2 = part2 + ff[i]

Integral = (3 / 8) * h * (fa + fb + 2 * mult3 + 3 * part2)
print("La integral es: ",Integral," atm*L")
v = Integral * (101.325 / 1000)
print("Equivalente a: ",v," kJ ")