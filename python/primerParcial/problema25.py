psi = 0.42748
omega = 0.08664
Pc = 37.96
P = 9.4573
Tc = 425.1
T = 350
Tr = T / Tc
Pr = P / Pc
q = (psi / omega) * (Tr**(-3 / 2))
B = omega * (Pr / Tr)
print
print("vapor saturado")
print
ep = 100
i = 0
Z0vs = 1
while ep > 0.001:
    Zvs = 1 + B - (q * B) * ((Z0vs - B) / (Z0vs * (Z0vs + B)))
    ep = abs((Zvs - Z0vs) / Zvs) * 100
    i = i + 1
    print("Número de iteración "+ str(i)+" , Z= "+ str(Zvs)+ ", ep= "+ str(ep))
    Z0vs = Zvs

print
print("El factor de compresibilidad para vapor saturado "+ str(Zvs)+", con un error relativo porcentual de: "+ str(ep))
print
print("Líquido saturado")
print
ep = 100
i = 0
Z0ls = 0.01
while ep > 0.001:
    Zls = B + ((Z0ls * (Z0ls + B) * (1 + B - Z0ls)) / (q * B))
    ep = abs((Zls - Z0ls) / Zls) * 100
    i = i + 1
    print("Número de iteración "+ str(i) + ", Z= "+ str(Zls)+ ", ep= "+ str(ep))
    Z0ls = Zls

print
print("El factor de compresibilidad para liquido saturado "+ str(Zls) +", con un error relativo porcentual de: "+ str(ep))
