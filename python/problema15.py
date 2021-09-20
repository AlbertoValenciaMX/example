import math

Q1 = 1
Q2 = 0
Q3 = 0
Q4 = 0
Q5 = 0
Q6 = 0
Q7 = 1
Q8 = 0
Q9 = 0
i = 0;
dfQ = 0
fQ = 1
qn7 = 0
while fQ > 0.01 or fQ < -0.01:
    fQ = 1 - (5.59586530386363 * (Q7)) - (10.2426406871193 * ((Q7)**2))
    dfQ = -(5.59586530386363) - (2 * 10.2426406871193 * (Q7))
    qn7 = Q7 - (fQ / dfQ)
    i = i + 1
    print("iteración "+str(i)+ " x=", str( qn7))
    Q7 = qn7
Q4 = math.sqrt(5 + 2 * (math.sqrt(2))) * (Q7)
Q5 = (1 + (math.sqrt(2))) * Q7
Q6 = (math.sqrt(2)) * Q7
Q3 = Q4 + Q5
Q2 = 1 - Q3
Q8 = Q5
Q9 = Q3
print("Q9= ",Q9)
print("Q8= ",Q8)
print("Q7= ",Q7)
print("Q6= ",Q6)
print("Q5= ",Q5)
print("Q4= ",Q4)
print("Q3= ",Q3)
print("Q2= ",Q2)
print("Q1= ",Q1)
print("SEGUNDA PARTE")
f1 = 0
a = (4 * Q1) / (math.pi * 0.0000179 * 0.5)
i = 0;
x1 = 3
x2 = 0
fc = 1
i = 0
while fc > 0.0001 or fc < -0.0001:
    fx1 = 4 * math.log10(a * (x1**0.5)) - 0.4 - (1 / (x1**0.5))
    fx2 = 4 * math.log10(a * (x2**0.5)) - 0.4 - (1 / (x2**0.5))
    f1 = (x1 + x2) / 2
    fc1 = 4 * math.log10(a * (f1**0.5)) - 0.4 - (1 / (f1**0.5))
    i = i + 1
    fc = fc1
    r1 = fc1 * fx1
    r2 = fc1 * fx2
    if r1 > 0:
        x1 = f1
    if r2 > 0:
        x2 = f1
f2 = 0
a = (4 * Q2) / (math.lpi * 0.0000179 * 0.5)
i = 0;
x1 = 3
x2 = 0
fc = 1
i = 0
while fc > 0.0001 or fc < -0.0001:
    fx1 = 4 * math.log10(a * (x1**0.5)) - 0.4 - (1 / (x1**0.5))
    fx2 = 4 * math.log10(a * (x2**0.5)) - 0.4 - (1 / (x2**0.5))
    f2 = (x1 + x2) / 2
    fc1 = 4 * math.log10(a * (f2**0.5)) - 0.4 - (1 / (f2**0.5))
    i = i + 1
    fc = fc1
    r1 = fc1 * fx1
    r2 = fc1 * fx2
    if r1 > 0:
        x1 = f2
    if r2 > 0:
        x2 = f2
f3 = 0
a = (4 * Q3) / (math.lpi * 0.0000179 * 0.5)
i = 0;
x1 = 3
x2 = 0
fc = 1
i = 0
while fc > 0.0001 or fc < -0.0001:
    fx1 = 4 * math.log10(a * (x1**0.5)) - 0.4 - (1 / (x1**0.5))
    fx2 = 4 * math.log10(a * (x2**0.5)) - 0.4 - (1 / (x2**0.5))
    f3 = (x1 + x2) / 2
    fc1 = 4 * math.log10(a * (f3**0.5)) - 0.4 - (1 / (f3**0.5))
    i = i + 1
    fc = fc1
    r1 = fc1 * fx1
    r2 = fc1 * fx2
    if r1 > 0:
        x1 = f3
    if r2 > 0:
        x2 = f3
f4 = 0
a = (4 * Q4) / (math.lpi * 0.0000179 * 0.5)
i = 0;
x1 = 3
x2 = 0
fc = 1
i = 0
while fc > 0.0001 or fc < -0.0001:
    fx1 = 4 * math.log10(a * (x1**0.5)) - 0.4 - (1 / (x1**0.5))
    fx2 = 4 * math.log10(a * (x2**0.5)) - 0.4 - (1 / (x2**0.5))
    f4 = (x1 + x2) / 2
    fc1 = 4 * math.log10(a * (f4**0.5)) - 0.4 - (1 / (f4**0.5))
    i = i + 1
    fc = fc1
    r1 = fc1 * fx1
    r2 = fc1 * fx2
    if r1 > 0:
        x1 = f4
    if r2 > 0:
        x2 = f4
f5 = 0
a = (4 * Q5) / (math.lpi * 0.0000179 * 0.5)
i = 0;
x1 = 3
x2 = 0
fc = 1
i = 0
while fc > 0.0001 or fc < -0.0001:
    fx1 = 4 * math.log10(a * (x1**0.5)) - 0.4 - (1 / (x1**0.5))
    fx2 = 4 * math.log10(a * (x2**0.5)) - 0.4 - (1 / (x2**0.5))
    f5 = (x1 + x2) / 2
    fc1 = 4 * math.log10(a * (f5**0.5)) - 0.4 - (1 / (f5**0.5))
    i = i + 1
    fc = fc1
    r1 = fc1 * fx1
    r2 = fc1 * fx2
    if r1 > 0:
        x1 = f5
    if r2 > 0:
        x2 = f5
f6 = 0
a = (4 * Q6) / (math.lpi * 0.0000179 * 0.5)
i = 0;
x1 = 3
x2 = 0
fc = 1
i = 0
while fc > 0.0001 or fc < -0.0001:
    fx1 = 4 * math.log10(a * (x1**0.5)) - 0.4 - (1 / (x1**0.5))
    fx2 = 4 * math.log10(a * (x2**0.5)) - 0.4 - (1 / (x2**0.5))
    f6 = (x1 + x2) / 2
    fc1 = 4 * math.log10(a * (f6**0.5)) - 0.4 - (1 / (f6**0.5))
    i = i + 1
    fc = fc1
    r1 = fc1 * fx1
    r2 = fc1 * fx2
    if r1 > 0:
        x1 = f6
    if r2 > 0:
        x2 = f6
f7 = 0
a = (4 * Q7) / (math.lpi * 0.0000179 * 0.5)
i = 0;
x1 = 3
x2 = 0
fc = 1
i = 0
while fc > 0.0001 or fc < -0.0001:
    fx1 = 4 * math.log10(a * (x1**0.5)) - 0.4 - (1 / (x1**0.5))
    fx2 = 4 * math.log10(a * (x2**0.5)) - 0.4 - (1 / (x2**0.5))
    f7 = (x1 + x2) / 2
    fc1 = 4 * math.log10(a * (f7**0.5)) - 0.4 - (1 / (f7**0.5))
    i = i + 1
    fc = fc1
    r1 = fc1 * fx1
    r2 = fc1 * fx2
    if r1 > 0:
        x1 = f7
    if r2 > 0:
        x2 = f7
f8 = 0
a = (4 * Q8) / (math.lpi * 0.0000179 * 0.5)
i = 0
x1 = 3
x2 = 0
fc = 1
i = 0
while fc > 0.0001 or fc < -0.0001:
    fx1 = 4 * math.log10(a * (x1**0.5)) - 0.4 - (1 / (x1**0.5))
    fx2 = 4 * math.log10(a * (x2**0.5)) - 0.4 - (1 / (x2**0.5))
    f8 = (x1 + x2) / 2
    fc1 = 4 * math.log10(a * (f8**0.5)) - 0.4 - (1 / (f8**0.5))
    i = i + 1
    fc = fc1
    r1 = fc1 * fx1
    r2 = fc1 * fx2
    if r1 > 0:
        x1 = f8
    if r2 > 0:
        x2 = f8
f9 = 0
a = (4 * Q9) / (math.lpi * 0.0000179 * 0.5)
i = 0;
x1 = 3
x2 = 0
fc = 1
i = 0
while fc > 0.0001 or fc < -0.0001:
    fx1 = 4 * math.log10(a * (x1**0.5)) - 0.4 - (1 / (x1**0.5))
    fx2 = 4 * math.log10(a * (x2**0.5)) - 0.4 - (1 / (x2**0.5))
    f9 = (x1 + x2) / 2
    fc1 = 4 * math.log10(a * (f9**0.5)) - 0.4 - (1 / (f9**0.5))
    i = i + 1
    fc = fc1
    r1 = fc1 * fx1
    r2 = fc1 * fx2
    if r1 > 0:
        x1 = f9
    if r2 > 0:
        x2 = f9
print("f1= ", f1)
print("f2= ", f2)
print("f3= ", f3)
print("f4= ", f4)
print("f5= ", f5)
print("f6= ", f6)
print("f7= ", f7)
print("f8= ", f8)
print("f9= ", f9)