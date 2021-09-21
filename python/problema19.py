t12 = 0
t22 = 0
t21 = 0
t11 = 0
E = 100
x = 0
a = 75
b = 25
c = 0
d = 200
while E > 0.0001:
    t12 = (b + d + t22 + t11) / 4
    t22 = (b + c + t21 + t12) / 4
    t11 = (t12 + t21 + a + d) / 4
    t21 = (t22 + c + a + t11) / 4
    E = abs((t12 - x) / t12)
    x = t12

print("Las temperaturas de los nodos son:")
print("T12 = ", t12)
print("T22 = ", t22)
print("T21 = ", t21)
print("T11 = ", t11)