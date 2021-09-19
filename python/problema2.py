import math

T = 0
x1 = 0.1
for t in range(1, 60):
    for k in range(1, 100):
        T = T + (4 / ((2 * k - 1) * math.pi)) * math.sin((2 * k - 1) *
                                                         math.pi * x1) * math.exp(-1 * (2 * k - 1) ** 2 * math.pi ** 2 * t)
        print(T)
print("En un tiempo de 60 segundos la temperatura alcanzada en x =", x1, " es de: ", T)
T = 0
x1 = 0.25
for t in range(1, 60):
    for k in range(1, 100):
        T = T + (4 / ((2 * k - 1) * math.pi)) * math.sin((2 * k - 1) *
                                                         math.pi * x1) * math.exp(-1 * (2 * k - 1) ** 2 * math.pi ** 2 * t)
print("En un tiempo de 60 segundos la temperatura alcanzada en x =", x1, " es de: ", T)
T = 0
x1 = 0.5
for t in range(1, 60):
    for k in range(1, 100):
        T = T + (4 / ((2 * k - 1) * math.pi)) * math.sin((2 * k - 1) *
                                                         math.pi * x1) * math.exp(-1 * (2 * k - 1) ** 2 * math.pi ** 2 * t)
print("En un tiempo de 60 segundos la temperatura que se alcanza en x= ",
      x1, " es de: ", T)
T = 0
x1 = 0.75
for t in range(1, 60):
    for k in range(1, 100):
        T = T + (4 / ((2 * k - 1) * math.pi)) * math.sin((2 * k - 1) *
                                                         math.pi * x1) * math.exp(-1 * (2 * k - 1) ** 2 * math.pi ** 2 * t)
print("En un tiempo de 60 segundos la temperatura alcanzada en x =", x1, " es de: ", T)
T = 0
x1 = 0.9
for t in range(1, 60):
    for k in range(1, 100):
        T = T + (4 / ((2 * k - 1) * math.pi)) * math.sin((2 * k - 1) *
                                                         math.pi * x1) * math.exp(-1 * (2 * k - 1) ** 2 * math.pi ** 2 * t)
print("En un tiempo de 60 segundos la temperatura alcanzada en x =", x1, " es de: ", T)
