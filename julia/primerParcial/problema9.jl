# Ecuacion 1
XC1 = 0
qn1 = 1000
er1 = 100
XA1 = 100
while er1 < -0.01 || er1 > 0.01
    global eq1 = (0.0016 * XC1^3) - (0.112 * XC1^2) + (3.6 * XC1) - 15
    global eqd1 = (0.0048 * XC1^2) - (0.224 * XC1) + 3.6
    global XA1 = XC1 - (eq1 / eqd1)
    global er1 = (eq1 - qn1) / eqd1
    global XC1 = XA1
    global qn1 = eq1
end
println("El número de moles que se producen de C debido a la reacción 1 es: ", XA1)
println("Con un error de: ", er1)
# Ecuacion 2
XC2 = 0
qn2 = 1000
er2 = 100
XA2 = 100
while er2 < -0.01 || er2 > 0.01
    global eq2 = (0.037 * XC2^2) - (3.22 * XC2) + 13.5
    global eqd2 = (0.074 * XC2) - (3.22)
    global XA2 = XC2 - (eq2 / eqd2)
    global er2 = (eq2 - qn2) / eqd2
    global XC2 = XA2
    global qn2 = eq2
end
println("El número de moles que se producen de C debido a la reacción 2 es: ", XA2)
println("Con un error de: ", er2)
