a = 0.70
b = 0.99
Rc = 3
Fa = (a / (a - 1)) * ((Rc**((a - 1) / a)) - 1)
Fb = (b / (b - 1)) * ((Rc**((b - 1) / b)) - 1)
err = 100
Wx = 0
n = 0
while err >= 0.001:
    Wx = a - ((Fa * (a - b)) / (Fa - Fb))
    Wx1 = (Wx / (Wx - 1)) * ((Rc**((Wx - 1) / Wx)) - 1)
    if Wx1 == 0:
        print("La raíz exacta es: xR")
    if a < 0 and b > 0:
        a = Wx
        Fa = (a / (a - 1)) * ((Rc**((a - 1) / a)) - 1)
    if a > 0 and b > 0:
        b = Wx
        Fb = (b / (b - 1)) * ((Rc**((b - 1) / b)) - 1)
    n = n + 1
    err = abs(b - a) * 100 / (2**n)
print("La raíz aproximada es= ",Wx)
print("Error= ",err)
print("Iteraciones= ",n)
