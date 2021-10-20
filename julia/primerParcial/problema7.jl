p = 3
K = 0.05
xL = -0.5
xU = 0.5
fL = xL * sqrt((2 * p) / (2 + xL)) / (1 - xL) - K
fU = xU * sqrt((2 * p) / (2 + xU)) / (1 - xU) - K
er = 100
xN = 0
n = 0
while er >= 0.0001
    global xN = (xL + xU) / 2
    global fN = xN * sqrt(2 * p / (2 + xN)) / (1 - xN) - K
    a = fN * fU
    b = fN * fL
    if fN == 0
    end
    if a < 0 && b > 0
        global xL = xN
        global fL = xL * sqrt(2 * p / (2 + xL)) / (1 - xL) - K
    end
    if a > 0 && b < 0
        global xU = xN
        global fU = xU * sqrt(2 * p / (2 + xU)) / (1 - xU) - K
    end
    global n = n + 1
    global er = abs((xU - xL))
end
println("la raíz exacta es ", xN)
println("La raíz aproximada es ", xN, " con un error de ", er)
println("Número de iteraciones: ", n)
using PyPlot
xg = zeros(100)
f = zeros(100)
acum = -0.51
for i = 1:100
    global acum = acum + 0.01
    global xg[i] = acum
    global f[i] = xg[i] * sqrt(2 * p / (2 + xg[i])) / (1 - xg[i]) - K
end
figure(1)
plot(xg,f)
scatter(xN,fN)
grid("on")

plt.show()