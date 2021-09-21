import matplotlib.pyplot as plt
import numpy as np

X = [0, 1, 2, 3, 4, 5, 6]
Y = [0.1, 0.332, 1.102, 1.644, 2.453, 3.660, 5.460]
plt.scatter(X,Y,color="green",label="Datos")
plt.xlabel("X- Tiempo")
plt.ylabel("Y- Colonias de Bacterias")
Sx = 0
Sy = 0
Sx2 = 0
Sx3 = 0
Sx4 = 0
Sx5 = 0
Sx6 = 0
Sxy = 0
Sx2y = 0
Sx3y = 0
n = 7
rr = 0
SC3 = 0
SC4 = 0
for i in range(0,n):
    Sx = Sx + X[i]
    Sy = Sy + Y[i]
    Sx2 = Sx2 + (X[i]**2)
    Sx3 = Sx3 + (X[i]**3)
    Sx4 = Sx4 + (X[i]**4)
    Sx5 = Sx5 + (X[i]**5)
    Sx6 = Sx6 + (X[i]**6)
    Sxy = Sxy + (X[i] * Y[i])
    Sx2y = Sx2y + ((X[i]**2) * Y[i])
    Sx3y = Sx3y + ((X[i]**3) * Y[i])

yp = Sy / n
xp = Sx / n
A = [[n, Sx, Sx2, Sx3], [Sx, Sx2, Sx3, Sx4], [Sx2, Sx3, Sx4, Sx5], [Sx3, Sx4, Sx5, Sx6]]
B = [[Sy], [Sxy], [Sx2y], [Sx3y]]
R = np.dot(np.linalg.inv(A), B)
for i in range(0,n):
    SC3 = SC3 + (((Y[i]) - yp)**2)
    SC4 = SC4 + (((Y[i]) - R[1] - ((R[2]) * X[i]) - ((X[i]**2) * R[3]) - ((X[i]**3) * R[4]))**2)

YN = np.zeros(n)
for i in range(0,n):
    YN[i] = R[1] + (R[2] * X[i]) + (R[3] * (X[i]**2)) + (R[4] * (X[i]**3))

plt.plot(np.transpose(X), YN, color="blue", label="Polinomial: Tercer grado")
plt.leg(bbox_to_anchor=(0.1, 1), loc=2)
plt.grid("on")
print("La función es y= "+str(R[4])+"x**3 + "+str(R[3])+"x**2 + "+str(R[2])+"x + "+str(R[1]))
rr = (SC3 - SC4) / SC3
print("El coeficiente de determinacion (R**2) es de ", rr)
h = 0.001
def funf(x):
    f = (R[4] * (x**3)) + (R[3] * (x**2)) + (R[2] * (x)) + (R[1])
    return f

fpp = np.zeros(n)
for i in range(1,n):
    fpp[i] = ((-funf(X[i] + 2h)) + (8 * funf(X[i] + h)) - (8 * funf(X[i] - h)) + funf(X[i] -2h)) / 12h

miu = np.zeros(n)
for i in range(1,n):
    miu[i] = fpp[i] * (1 / (Y[i]))
    print("El valor de miu a t= ", X[i], " es de ", miu[i], " h**-1")

print("El valor de miu a t= ", X[3], " h es de ", miu[3], " h**-1")
print("El valor de miu a t= ", X[5], " h es de ", miu[5], " h**-1")
print("El valor de miu a t= ", X[7], " h es de ", miu[7], " h**-1")

plt.show()