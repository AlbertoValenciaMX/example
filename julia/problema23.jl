P = [0.1 5 10 20 25 30 40 45 50]
Temp = [350 400 450]
VT350 = [220 4.1 2.2 1.35 1.1 0.9 0.68 0.61 0.54]
VT400 = [250 4.7 2.5 1.49 1.2 0.99 0.75 0.675 0.6]
VT450 = [282.5 5.23 2.7 1.55 1.24 1.03 0.78 0.7 0.62]
Sxy = 0
Sx = 0
Sy = 0
Sy2 = 0
Sx2 = 0
Sx3 = 0
Sx4 = 0
Sx5 = 0
Sx6 = 0
Sx2y = 0
Sx3y = 0
n = 9
Bet = zeros(n)
for i = 1:n
    Bet[i] = ((VT450[i] - VT350[i]) / (Temp[3] - Temp[1])) / (VT400[i])
end
V = zeros(n)
for i = 1:n
    global V[i] = VT400[i] * (1 - Temp[2] * Bet[i])
    global Sxy = Sxy + (P[i] * V[i])
    global Sx = Sx + P[i]
    global Sy = Sy + V[i]
    global Sy2 = Sy2 + (V[i]^2)
    global Sx2 = Sx2 + (P[i]^2)
    global Sx3 = Sx3 + (P[i]^3)
    global Sx4 = Sx4 + (P[i]^4)
    global Sx5 = Sx5 + (P[i]^5)
    global Sx6 = Sx6 + (P[i]^6)
    global Sx2y = Sx2y + ((P[i]^2) * V[i])
    global Sx3y = Sx3y + ((P[i]^3) * V[i])
end
yp = Sy / n
xp = Sx / n
A = [n Sx Sx2 Sx3;Sx Sx2 Sx3 Sx4;Sx2 Sx3 Sx4 Sx5;Sx3 Sx4 Sx5 Sx6]
B = [Sy ;Sxy ;Sx2y ;Sx3y]
C = inv(A) * B
a = P[1]
b = P[9]
N = 11
N2 = N - 1
h = (b - a) / N2
mult3 = 0
part2 = 0
fa = C[4] * (a^3) + C[3] * (a^2) + C[2] * (a) + C[1]
fb = C[4] * (b^3) + C[3] * (b^2) + C[2] * (b) + C[1]
ff = zeros(N2)
x = a
for i = 1:N2
    global x = x + h
    global ff[i] = C[4] * (x^3) + C[3] * (x^2) + C[2] * (x) + C[1]
    println("Iteración: ", i, ", X= ", x, ", f(x)= ", ff[i])
end
for i = 2:1:N2 - 1
    if i % 3 == 0
        global mult3 = mult3 + ff[i]
    else
        global part2 = part2 + ff[i]
    end
end
Integral = (3 / 8) * h * (fa + fb + 2 * mult3 + 3 * part2)
println("La integral es: ",Integral," atm*L")
v = Integral * (101.325 / 1000)
println("Equivalente a: ",v," kJ ")