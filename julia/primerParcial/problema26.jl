C0 = 3
k = 2
a = 0
b = 60
n = 400
h = (b - a) / n
t = zeros(n + 1)
C = zeros(n + 1)
C[1] = C0
t[1] = 0
for i = 1:n
    global fxy = (-k * (C[i]^2))
    global C[i + 1] = C[i] + (h * fxy)
    global t[i + 1] = t[i] + h
    println("Iteración ", i, " [C] = ", C[i + 1], " en un tiempo de = ", t[i + 1], " fxy = ", fxy)
end
println("La concentración [C]= ",C[n]," mol/L, corresponde cuando pasan ",t[n]," segundos = ", t[n] / 60," minutos ")
using PyPlot
figure(1)
plot(t,C,label="Concentración")
scatter(t,C)
xlabel("t Tiempo (seg)")
ylabel("C Concentración (mol/L)")
grid("on")
legend(bbox_to_anchor=(0.1, 1), loc=2)

plt.show()