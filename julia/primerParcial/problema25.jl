psi = 0.42748
omega = 0.08664
Pc = 37.96
P = 9.4573
Tc = 425.1
T = 350
Tr = T / Tc
Pr = P / Pc
q = (psi / omega) * (Tr^(-3 / 2))
B = omega * (Pr / Tr)
println("\n")
println("vapor saturado")
println("\n")
ep = 100
i = 0
Z0vs = 1
while ep > 0.001
    global Zvs = 1 + B - (q * B) * ((Z0vs - B) / (Z0vs * (Z0vs + B)))
    global ep = abs((Zvs - Z0vs) / Zvs) * 100
    global i = i + 1
    println("Número de iteración ", i, " , Z= ", Zvs, ", ep= ", ep)
    global Z0vs = Zvs
end
println("\n")
println("El factor de compresibilidad para vapor saturado ",Zvs,", con un 
error relativo porcentual de: ",ep,"\n")
println("\n")
println("Líquido saturado")
println("\n")
ep = 100
i = 0
Z0ls = 0.01
while ep > 0.001
    global Zls = B + ((Z0ls * (Z0ls + B) * (1 + B - Z0ls)) / (q * B))
    global ep = abs((Zls - Z0ls) / Zls) * 100
    global i = i + 1
    println("Número de iteración ", i, ", Z= ", Zls, ", ep= ", ep)
    global Z0ls = Zls
end
println("\n")
println("El factor de compresibilidad para liquido saturado ",Zls,", con un error relativo porcentual de: ",ep)
