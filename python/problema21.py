import matplotlib.pyplot as plt
import numpy as np
import math

T = [595, 623, 761, 849, 989, 1076, 1146, 1202, 1382, 1445, 1562]
k = [2.12, 3.12, 14.4, 30.6, 80.3, 131, 186, 240, 489, 604, 868]

plt.scatter(T,k,color="green",label="Datos")
plt.xlabel("Temperatura (K)")
plt.ylabel("k")
n = 11
SlnT = 0
SinvT = 0
SlnTc = 0
SlnTinvT = 0
SinvTc = 0
Slnk = 0
SlnTlnk = 0
SinvTlnk = 0
for i in range(1,n):
    SlnT = SlnT + math.log(T[i])
    SinvT = SinvT + (-1 / T[i])
    SlnTc = SlnTc + ((math.log(T[i]))**2)
    SlnTinvT = SlnTinvT + ((math.log(T[i])) * (-1 / T[i]))
    SinvTc = SinvTc + ((-1 / T[i])**2)
    Slnk = Slnk + math.log(k[i])
    SlnTlnk = SlnTlnk + ((math.log(T[i])) * (math.log(k[i])))
    SinvTlnk = SinvTlnk + ((-1 / T[i]) * (math.log(k[i])))

A = [[n, SlnT, SinvT],[SlnT, SlnTc, SlnTinvT], [SinvT, SlnTinvT, SinvTc]]
B = [[Slnk], [SlnTlnk], [SinvTlnk]]
R = np.dot(np.linalg.inv(A), B)
plt.leg(bbox_to_anchor=(0.1, 1), loc=2)
plt.grid("on")

print("La función es ln(k)= "+str(R[1])+" + "+ str(R[2])+" ln(T) + "+ str(R[3]) +"/T")
print(" donde b= "* str(R[2])+ ", C= "+ str(R[1])+ ", D= " + str(R[3]))

plt.show()