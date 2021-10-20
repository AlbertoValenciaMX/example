y = [1.787e-3 1.519e-3 1.307e-3 1.002e-3 7.975e-4 6.529e-4 4.665e-4 3.547e-4 2.828e-4]
x = [273.15 278.15 283.15 293.15 303.15 313.15 333.15 353.15 373.15]
m = 4
n = 9
xi = 0
yi = 0
xi2 = 0
xi3 = 0
xi4 = 0
xi5 = 0
xi6 = 0
xi7 = 0
xi8 = 0
xiyi = 0
xi2yi = 0
xi3yi = 0
xi4yi = 0
a0 = a1 = a2 = a3 = a4 = 1
for i = 1:n
    global xi = xi + (x[i])
    global yi = yi + (y[i])
    global xi2 = xi2 + (x[i]^2)
    global xi3 = xi3 + (x[i]^3)
    global xi4 = xi4 + (x[i]^4)
    global xi5 = xi5 + (x[i]^5)
    global xi6 = xi6 + (x[i]^6)
    global xi7 = xi7 + (x[i]^7)
    global xi8 = xi8 + (x[i]^8)
    global xiyi = xiyi + (x[i] * y[i])
    global xi2yi = xi2yi + ((x[i]^2) * y[i])
    global xi3yi = xi3yi + ((x[i]^3) * y[i])
    global xi4yi = xi4yi + ((x[i]^4) * y[i])
end
E = [n xi xi2 xi3 xi4;xi xi2 xi3 xi4 xi5;xi2 xi3 xi4 xi5 xi6;xi3 xi4 xi5 xi6 xi7;xi4 xi5 xi6 xi7 xi8]
M = [yi;xiyi;xi2yi;xi3yi;xi4yi]
z = inv(E) * M
A = 0.4892920416314155
B = -0.0056890474184001505
C = 2.4915226980226635e-5
D = -4.861560886151861e-8
E = 3.56198345152119e-11
println("Valores de las constantes de la relación desarrollada ")
println(z)
println("Valor de A: ",A)
println("Valor de B: ",B)
println("Valor de C: ",C)
println("Valor de D: ",D)
println("Valor de E: ",E)