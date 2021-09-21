import matplotlib.pyplot as plt
import numpy as np

x = [[10],[15],[20],[25],[40],[50],[55],[60],[75]]
y = [[5],[20],[18],[40],[33],[54],[70],[60],[78]]
plt.scatter(x,y, color="red", label="datos")
plt.grid("on")
n = 9
xyi = 0
xi = 0
yi = 0
xi2 = 0
# Sumatorias
for i in range(1,n):
    xyi = xyi + (x[i] * y[i])
    xi = xi + x[i]
    yi = yi + y[i]
    xi2 = xi2 + (x[i]**2)

a1 = (n * xyi - xi * yi) / (n * xi2 - xi**2)
xp = xi / n
yp = yi / n
a0 = yp - a1 * xp
print(" a0 = "+str(a0)+", a1 = "+str(a1))
# función
f = np.zeros(n)
for i in range(0,n):
    f[i] = a1 * x[i] + a0

plt.plot(x,f)
print("La ecuación resultante es y = "+str(a1)+"x + "+str(a0))
# Evaluar función en 32 min
mn = 32
fp = a1 * mn + a0
print("El esfuerzo de tensión en "+str(mn)+" min es de "+str(fp))
plt.scatter(mn,fp,color="purple", label="32min")
plt.leg(bbox_to_anchor=(0.1, 1), loc=2)

plt.show()