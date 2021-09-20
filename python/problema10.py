import math

d = 1.23
u = 0.0000179
D = 0.005
V = 40
E = 0.0000015
E2 = 0.000045
a = 0.0001
b = 0.3
Re = (d * V * D) / u
Fa = -2 * math.log((E / 3.7 * D) + (2.51 / Re * math.sqrt(a))) - (1 / math.sqrt(a))
Fb = -2 * math.log((E / 3.7 * D) + (2.51 / Re * math.sqrt(b))) - (1 / math.sqrt(b))
err = 100
Wx = 0
n = 0
while err >= 0.0008:
    Wx = b - ((Fb * (a - b)) / (Fa - Fb))
    Wx1 = -2 * math.log((E / 3.7 * D) + (2.51 / Re * math.sqrt(Wx))) - (1 / math.sqrt(Wx))
    if Wx1 == 0:
        print("La raíz exacta es:"+ xR)
    if a < 0 and b > 0:
        a = Wx
        Fa = -2 * math.log((E / 3.7 * D) + (2.51 / Re * math.sqrt(a))) - (1 / math.sqrt(a))
    if a > 0 and b > 0:
        b = Wx
        Fb = -2 * math.log((E / 3.7 * D) + (2.51 / Re * math.sqrt(b))) - (1 / math.sqrt(b))
    n = n + 1
    err = abs(b - a) * 100 / (2**n)
print("*********E = 0.0015 mm**********")
print("La raíz aproximada es: ", Wx)
print("Error =: ",err)
print("Iteraciones =: ",n)
print("NRe = ",Re)
d2 = 1.23
u2 = 0.0000179
D2 = 0.005
V2 = 40
E2 = 0.000045
a2 = 0.0001
b2 = 0.3
Re2 = (d2 * V2 * D2) / u2
Fa2 = -2 * math.log((E2 / 3.7 * D2) + (2.51 / Re2 * math.sqrt(a2))) - (1 / math.sqrt(a2))
Fb2 = -2 * math.log((E2 / 3.7 * D2) + (2.51 / Re2 * math.sqrt(b2))) - (1 / math.sqrt(b2))
err2 = 100
Wx2 = 0
n2 = 0
while err2 >= 0.0008:
    Wx2 = b2 - ((Fb2 * (a2 - b2)) / (Fa2 - Fb2))
    Wx3 = -2 * math.log((E2 / 3.7 * D2) + (2.51 / Re2 * math.sqrt(Wx2))) - (1 / math.sqrt(Wx2))
    if Wx3 == 0:
        print("La raíz exacta es:", xR2)
    if a2 < 0 and b2 > 0:
        a2 = Wx2
        Fa2 = -2 * math.log((E2 / 3.7 * D2) + (2.51 / Re2 * math.sqrt(a2))) - (1 / math.sqrt(a2))
    if a2 > 0 and b2 > 0:
        b2 = Wx2
        Fb2 = -2 * math.log((E2 / 3.7 * D2) + (2.51 / Re2 * math.sqrt(b2))) - (1 / math.sqrt(b2))
    n2 = n2 + 1
    err2 = abs(b2 - a2) * 100 / (2**n2)
print("*********E2 = 0.045 mm**********")
print("La raíz aproximada es: ", Wx2)
print("Error2 =: ",err2)
print("Iteraciones =: ",n2)
print("NRe = ",Re2)
