A = [120 -20 1;-80 80 1;-40 -60 120]
B = [400;0;200]
x = inv(A) * B
println("Las concentraciones son:")
println("C1= ",x[1])
println("C2= ",x[2])
println("C3= ",x[3])