# clearconsole()
using PyPlot
d = 3
TenF = zeros(d)
TenC = zeros(d)
TenF[1] = 20
TenF[2] = 40
TenF[3] = 60
n = 401
TeqF = zeros(n)
TeqC = zeros(n)
VF = zeros(n)
VC = zeros(n)
VF[1] = 4
for j = 1:d
    global TenC[j] = (TenF[j] - 32) * 5 / 9
    for i = 1:n - 1
        global VC[i] = VF[i] * 1.60934
        global TeqF[i] = (91.4 - (91.4 - TenF[j])) * (0.0475 -
0.0203 * VF[i] + 0.304 * sqrt(VF[i]))
        global TeqC[i] = ((91.4 - 32) * 5 / 9 - ((91.4 - 32) * 5 / 9 -
TenC[j])) * (0.0475 * 1.60934 - 0.0203 * VC[i] + 0.304 * sqrt(VC[i])) * 9 / 5 + 32
        global VF[i + 1] = VF[i] + 0.1
    end
    figure("En unidades originales problema ")
    scatter(TeqF, VF)
    xlabel("T equivalente en ºF")
    ylabel("Velocidad del aire en millas/h")
    figure("En unidades SI")
    scatter(TeqC, VC)
    xlabel("T equivalente en ºC")
    ylabel("Velocidad del aire en km/h")
end