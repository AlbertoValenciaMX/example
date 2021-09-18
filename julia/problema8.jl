p = 1.367887 # MPa
a = 1.39
b = 0.03913
R = 0.008314
T = 293.15
n = 1.5
# Sustituyendo los valores de los datos en la ecuacion de Van Der Waals y simplificando nos queda la funcion siguiente fv=13.5*(v^3)-
# 4.44825615*(v*2)+5.483810475*v-0.32180610076 que resolveremos por NewRap
v = 0.06116
fv = 1
i = 0
while fv > 0.01 || fv < -0.01
    global fv = (1.367888 * (v^3)) - (3.73616165 * (v * 2)) + (5.483810475 * v) -
0.321872
    global dfv = (4.103664 * (v^2)) - (7.4723233 * v) + 5.483810475
    global v = v - (fv / dfv)
    global i = i + 1
    println("iteración ", i, " v=", v)
end
println("El volumen del recipiente es ",v, " litros")
