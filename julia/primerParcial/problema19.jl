t12 = 0
t22 = 0
t21 = 0
t11 = 0
E = 100;x = 0
a = 75;b = 25;c = 0;d = 200
while E > 0.0001
    global t12 = (b + d + t22 + t11) / 4
    global t22 = (b + c + t21 + t12) / 4
    global t11 = (t12 + t21 + a + d) / 4
    global t21 = (t22 + c + a + t11) / 4
    global E = abs((t12 - x) / t12)
    global x = t12
end
println("Las temperaturas de los nodos son:")
println("T12 = ",t12)
println("T22 = ",t22)
println("T21 = ",t21)
println("T11 = ",t11)
