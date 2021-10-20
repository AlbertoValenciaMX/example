T = [595 623 761 849 989 1076 1146 1202 1382 1445 1562]
k = [2.12 3.12 14.4 30.6 80.3 131 186 240 489 604 868]
using PyPlot
scatter(T,k,color="green",label="Datos")
xlabel("Temperatura (K)")
ylabel("k")
n = 11
SlnT = 0
SinvT = 0
SlnTc = 0
SlnTinvT = 0
SinvTc = 0
Slnk = 0
SlnTlnk = 0
SinvTlnk = 0
for i = 1:n
    global SlnT = SlnT + log(T[i])
    global SinvT = SinvT + (-1 / T[i])
    global SlnTc = SlnTc + ((log(T[i]))^2)
    global SlnTinvT = SlnTinvT + ((log(T[i])) * (-1 / T[i]))
    global SinvTc = SinvTc + ((-1 / T[i])^2)
    global Slnk = Slnk + log(k[i])
    global SlnTlnk = SlnTlnk + ((log(T[i])) * (log(k[i])))
    global SinvTlnk = SinvTlnk + ((-1 / T[i]) * (log(k[i])))
end
A = [n SlnT SinvT;SlnT SlnTc SlnTinvT;SinvT SlnTinvT SinvTc]
B = [Slnk; SlnTlnk; SinvTlnk]
R = inv(A) * B
legend(bbox_to_anchor=(0.1, 1), loc=2)
grid("on")

println("La función es ln(k)= ",R[1]," + ",R[2]," ln(T) + ",R[3],"/T")
println(" donde b= ", R[2], ", C= ", R[1], ", D= ", R[3])

plt.show()