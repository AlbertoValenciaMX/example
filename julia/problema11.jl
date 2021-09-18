cp1 = 2300
m2 = 5
m1 = 3 + 0.75 * m2
cp2 = 4000
Tci = 0
Thi = 50
Th0 = 100
Tc0 = 15
Q = 1000000
n = 0
U = 400
i = 0
n = 4
B = 0
Ap = 0
incre = 2.5
using PyPlot
clearconsole()
Tci = zeros(n + 1);A = zeros(n + 1)
for i in 0:n
    global Tci[i + 1] = (Q / (m1 * cp1)) + (Tc0)
    println("Tc", i + 1, "= ", Tci[i + 1])
    global delT = ((Thi - Tc0) - (Th0 - Tci[i + 1])) / log((Thi - Tc0) / (Th0 - Tci[i + 1]))
    println("Delta T",i + 1,"= ",delT)
    global A[i + 1] = Q / (U * delT)
    println("A",i + 1,"= ",A[i + 1])
    println()
    global B = B + A[i + 1]
    global Tc0 = Tc0 + incre
end
global Ap = B / (n + 1)
println("Área promedio= ",Ap)
figure("gráfica de temperaturas")
plot(A,Tci,color="green")
scatter(A,Tci,color="purple")
xlabel("Área de transferencia")
ylabel("Temperatura de entrada")
grid("on")

plt.show()