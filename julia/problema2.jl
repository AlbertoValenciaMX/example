T = 0
x1 = 0.1
for t = 1:60
    for k = 1:100
        global T = T + (4 / ((2 * k - 1) * pi)) * sind((2 * k - 1) * pi * x1) * exp(-1 * (2 * k - 1)^2 * pi^2 * t)
        println(T)
    end
end
println("\n")
println("En un tiempo de 60 segundos la temperatura alcanzada en x =
",x1," es de: ",T)
T = 0
x1 = 0.25
for t = 1:60
    for k = 1:100
        global T = T + (4 / ((2 * k - 1) * pi)) * sind((2 * k - 1) * pi * x1) * exp(-1 * (2 * k - 1)^2 * pi^2 * t)
    end
end
println("En un tiempo de 60 segundos la temperatura alcanzada en x =
",x1," es de: ",T)
T = 0
x1 = 0.5
for t = 1:60
    for k = 1:100
        global T = T + (4 / ((2 * k - 1) * pi)) * sind((2 * k - 1) * pi * x1) * exp(-1 * (2 * k - 1)^2 * pi^2 * t)
    end
end
println("En un tiempo de 60 segundos la temperatura que se alcanza en x
= ",x1," es de: ",T)
T = 0
x1 = 0.75
for t = 1:60
    for k = 1:100
        global T = T + (4 / ((2 * k - 1) * pi)) * sind((2 * k - 1) * pi * x1) * exp(-1 * (2 * k - 1)^2 * pi^2 * t)
    end
end
println("En un tiempo de 60 segundos la temperatura alcanzada en x =
",x1," es de: ",T)
T = 0
x1 = 0.9
for t = 1:60
    for k = 1:100
        global T = T + (4 / ((2 * k - 1) * pi)) * sind((2 * k - 1) * pi * x1) * exp(-1 * (2 * k - 1)^2 * pi^2 * t)
    end
end
println("En un tiempo de 60 segundos la temperatura alcanzada en x =
",x1," es de: ",T)