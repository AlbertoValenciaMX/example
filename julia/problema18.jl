C1 = zeros(5, 5)
C1R = [1;0;0;0;0]
C1[1] = 1 
V = [25 75 100 25]
k = [0.05 0.1 0.5 0.1]
Ref = [0 0 5 3 0]
# balance
E = [1 0 0 0 0;-1 1 0 0 0;0 -1 1 0 0;0 0 -1 1 0; 0 0 0 -1 1]
R = [10; 0; 5; -2; -3]
Q = inv(E) * R 
# balance reactores
for i = 1:4
    global C1[i + 1,i] = Q[i] - Ref[i] - k[i] * V[i]
    global C1[i + 1,i + 1] = Ref[i + 1] - Q[i + 1]
end
C1s = inv(C1) * C1R
# No se pueden tener concentraciones negativas
for i = 1:5
    if C1s[i] < 0
        C1s[i] = 0
    end
end
println("Las corrientes del sistema son ",Q)
println("Las concentraciones de A en el reactor son ",C1s)