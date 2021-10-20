# Ecuacion 1
XC1 = 0
qn1 = 1000
er1 = 100
XA1 = 100
while er1 < -0.01 or er1 > 0.01:
    eq1 = (0.0016 * XC1 ** 3) - (0.112 * XC1 ** 2) + (3.6 * XC1) - 15
    eqd1 = (0.0048 * XC1 ** 2) - (0.224 * XC1) + 3.6
    XA1 = XC1 - (eq1 / eqd1)
    er1 = (eq1 - qn1) / eqd1
    XC1 = XA1
    qn1 = eq1
print("El número de moles que se producen de C debido a la reacción 1 es: " + str(XA1))
print("Con un error de: " + str(er1))
# Ecuacion 2
XC2 = 0
qn2 = 1000
er2 = 100
XA2 = 100
while er2 < -0.01 or er2 > 0.01:
    eq2 = (0.037 * XC2 ** 2) - (3.22 * XC2) + 13.5
    eqd2 = (0.074 * XC2) - (3.22)
    XA2 = XC2 - (eq2 / eqd2)
    er2 = (eq2 - qn2) / eqd2
    XC2 = XA2
    qn2 = eq2
print("El número de moles que se producen de C debido a la reacción 2 es: " + str(XA2))
print("Con un error de: " + str(er2))
