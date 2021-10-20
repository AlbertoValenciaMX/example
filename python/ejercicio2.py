#Problema 2
import matplotlib.pyplot as plt
import numpy as np
import math

T=np.array([79.7, 105.8, 120.0, 141.8, 178.5, 197.3])
P=np.array([5, 20, 40, 100, 400, 760.0])


plt.scatter(T,P,color="red",label="datos")
plt.xlabel("T - temperatura")
plt.ylabel("P - presion ")

Sxy=0
Sx=0
Sy=0
Sx2=0
Sy2=0
n=6

for i in range(0,n):
    Sxy=Sxy+(T[i]*P[i])
    Sx=Sx+T[i]
    Sy=Sy+P[i]
    Sx2=Sx2+(T[i]**2)
    Sy2=Sy2+(P[i]**2)

    beta1=((n*Sxy)-(Sx*Sy))/((n*Sx2)-(Sx**2))
    xp=Sx/n
    yp=Sy/n
    beta0=yp-(beta1*xp)

    YN=np.zeros(n)

    for i in range(0,n):
        YN[i]=(beta1*T[i])+beta0

plt.plot(np.transpose(T),YN,color="purple",label="lineal")

print("###########################################################")
print("la función es y = ",beta1," x + ",beta0)
r=((n*Sxy)-(Sx*Sy))/(math.sqrt(n*Sx2-(Sx**2))*math.sqrt(n*Sy2-(Sy**2)))
print("el factor de correlación (r) es de ",r)

Tl=np.zeros(n)
Pl=np.zeros(n)

for i in range(0,n):
    Tl[i]=math.log(T[i])
    Pl[i]=math.log(P[i])

Sxy=0
Sx=0
Sy=0
Sx2=0
Sy2=0
n=6

for i in range(0,n):
    Sxy=Sxy+(Tl[i]*Pl[i])
    Sx=Sx+Tl[i]
    Sy=Sy+Pl[i]
    Sx2=Sx2+(Tl[i]**2)
    Sy2=Sy2+(Pl[i]**2)


    beta1=((n*Sxy)-(Sx*Sy))/((n*Sx2)-(Sx**2))
    xp=Sx/n
    yp=Sy/n
    beta0=yp-(beta1*xp)

    YN=np.zeros(n)

    for i in range (0,n):
        YN[i]=math.exp(beta0)*(T[i]**beta1)

plt.plot(np.transpose(T),YN,color="green",label="potencia")
plt.legend(bbox_to_anchor=(0.1,1), loc=2)
plt.grid("on")

print("###########")
print("la función es y = ",math.exp(beta0)," * x ** ",beta1)
r=((n*Sxy)-(Sx*Sy))/(math.sqrt(n*Sx2-(Sx**2))*math.sqrt(n*Sy2-(Sy**2)))
print("el factor de correlación (r) es de ",r)

plt.show()