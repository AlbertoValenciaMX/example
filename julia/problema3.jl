miu = 0.38
D = 0.3 # m
w1 = 1450 # en rpm
w2 = 1398 # en rpm
w = 2 * pi * abs(w1 - w2) / 60 # Velocidad angular relativa
ls = 10
s = 0.1 / 1000
a = ls / s
h = zeros(100)
T = zeros(100)
for i = 1:99
    global h[i + 1] = h[i] + s
    global T[i + 1] = pi * miu * w * (D^4) / (32 * h[i + 1])
end
h[1] = 0.000099
T[1] = pi * miu * w * (D^4) / (32 * h[1])
using PyPlot
figure(1)
scatter(h,T,color="pink",label="")
plot(h,T)
grid("on")
println(" h = ", h[31]," T = ", T[31]) # valor medio

plt.show()