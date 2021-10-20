using PyPlot
x = [10;15;20;25;40;50;55;60;75]
y = [5;20;18;40;33;54;70;60;78]
scatter(x,y, color="red", label="datos")
grid("on")
n = 9
xyi = 0
xi = 0
yi = 0
xi2 = 0
# Sumatorias
for i = 1:n
    global xyi = xyi + (x[i] * y[i])
    global xi = xi + x[i]
    global yi = yi + y[i]
    global xi2 = xi2 + (x[i]^2)
end
a1 = (n * xyi - xi * yi) / (n * xi2 - xi^2)
xp = xi / n
yp = yi / n
a0 = yp - a1 * xp
println(" a0 = ",a0,", a1 = ",a1)
# función
f = zeros(n)
for i = 1:n
    global f[i] = a1 * x[i] + a0
end
plot(x,f)
println("La ecuación resultante es y = ",a1,"x + ",a0)
# Evaluar función en 32 min
mn = 32
fp = a1 * mn + a0
println("El esfuerzo de tensión en ",mn," min es de ",fp)
scatter(mn,fp,color="purple", label="32min")
legend(bbox_to_anchor=(0.1, 1), loc=2)

plt.show()