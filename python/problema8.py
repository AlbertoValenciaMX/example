p = 1.367887 # MPa
a = 1.39
b = 0.03913
R = 0.008314
T = 293.15
n = 1.5
# Sustituyo los valores de los datos en la ecuacion de Van Der Waals y simplificando nos queda la funcion siguiente fv=13.5*(v**3)-
# 4.44825615*(v*2)+5.483810475*v-0.32180610076 que resolveremos por NewRap
v = 0.06116
fv = 1
i = 0
while fv > 0.01 or fv < -0.01:
    fv = (1.367888 * (v**3)) - (3.73616165 * (v * 2)) + (5.483810475 * v) -0.321872
    dfv = (4.103664 * (v**2)) - (7.4723233 * v) + 5.483810475
    v = v - (fv / dfv)
    i = i + 1
    print("iteración ", i, " v=", v)
print("El volumen del recipiente es ",v, " litros")
