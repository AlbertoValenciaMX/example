d = 1.23
u = 0.0000179
D = 0.005
V = 40
E = 0.0000015
E2 = 0.000045
a = 0.0001
b = 0.3
Re = (d * V * D) / u
Fa = -2 * log((E / 3.7 * D) + (2.51 / Re * sqrt(a))) - (1 / sqrt(a))
Fb = -2 * log((E / 3.7 * D) + (2.51 / Re * sqrt(b))) - (1 / sqrt(b))
err = 100
Wx = 0
n = 0
while err >= 0.0008
    global Wx = b - ((Fb * (a - b)) / (Fa - Fb))
    global Wx1 = -2 * log((E / 3.7 * D) + (2.51 / Re * sqrt(Wx))) - (1 / sqrt(Wx))
    if Wx1 == 0
        println("La raíz exacta es:", xR)
    end
    if a < 0 && b > 0
        global a = Wx
        global Fa = -2 * log((E / 3.7 * D) + (2.51 / Re * sqrt(a))) - (1 / sqrt(a))
    end
    if a > 0 && b > 0
        global b = Wx
        global Fb = -2 * log((E / 3.7 * D) + (2.51 / Re * sqrt(b))) - (1 / sqrt(b))
    end
    global n = n + 1
    global err = abs(b - a) * 100 / (2^n)
end
println("*********E = 0.0015 mm**********")
println("La raíz aproximada es: ", Wx)
println("Error =: ",err)
println("Iteraciones =: ",n)
println("NRe = ",Re)
d2 = 1.23
u2 = 0.0000179
D2 = 0.005
V2 = 40
E2 = 0.000045
a2 = 0.0001
b2 = 0.3
Re2 = (d2 * V2 * D2) / u2
Fa2 = -2 * log((E2 / 3.7 * D2) + (2.51 / Re2 * sqrt(a2))) - (1 / sqrt(a2))
Fb2 = -2 * log((E2 / 3.7 * D2) + (2.51 / Re2 * sqrt(b2))) - (1 / sqrt(b2))
err2 = 100
Wx2 = 0
n2 = 0
while err2 >= 0.0008
    global Wx2 = b2 - ((Fb2 * (a2 - b2)) / (Fa2 - Fb2))
    global Wx3 = -2 * log((E2 / 3.7 * D2) + (2.51 / Re2 * sqrt(Wx2))) - (1 / sqrt(Wx2))
    if Wx3 == 0
        println("La raíz exacta es:", xR2)
    end
    if a2 < 0 && b2 > 0
        global a2 = Wx2
        global Fa2 = -2 * log((E2 / 3.7 * D2) + (2.51 / Re2 * sqrt(a2))) - (1 / sqrt(a2))
    end
    if a2 > 0 && b2 > 0
        global b2 = Wx2
        global Fb2 = -2 * log((E2 / 3.7 * D2) + (2.51 / Re2 * sqrt(b2))) - (1 / sqrt(b2))
    end
    global n2 = n2 + 1
    global err2 = abs(b2 - a2) * 100 / (2^n2)
end
println("\n")
println("*********E2 = 0.045 mm**********")
println("La raíz aproximada es: ", Wx2)
println("Error2 =: ",err2)
println("Iteraciones =: ",n2)
println("NRe = ",Re2)
