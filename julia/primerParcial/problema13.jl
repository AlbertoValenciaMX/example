a = 0.70
b = 0.99
Rc = 3
Fa = (a / (a - 1)) * ((Rc^((a - 1) / a)) - 1)
Fb = (b / (b - 1)) * ((Rc^((b - 1) / b)) - 1)
err = 100
Wx = 0
n = 0
while err >= 0.001
    global Wx = a - ((Fa * (a - b)) / (Fa - Fb))
    global Wx1 = (Wx / (Wx - 1)) * ((Rc^((Wx - 1) / Wx)) - 1)
    if Wx1 == 0
        println("La raíz exacta es:", xR)
    end
    if a < 0 && b > 0
        global a = Wx
        global Fa = (a / (a - 1)) * ((Rc^((a - 1) / a)) - 1)
    end
    if a > 0 && b > 0
        global b = Wx
        global Fb = (b / (b - 1)) * ((Rc^((b - 1) / b)) - 1)
    end
    global n = n + 1
    global err = abs(b - a) * 100 / (2^n)
end
println("La raíz aproximada es= ",Wx)
println("Error= ",err)
println("Iteraciones= ",n)
