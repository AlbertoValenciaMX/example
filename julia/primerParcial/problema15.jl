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
while fQ > 0.01 || fQ < -0.01
    global fQ = 1 - (5.59586530386363 * (Q7)) - (10.2426406871193 * ((Q7)^2))
    global dfQ = -(5.59586530386363) - (2 * 10.2426406871193 * (Q7))
    global qn7 = Q7 - (fQ / dfQ)
    global i = i + 1
    println("iteración ", i, " x=", qn7)
    global Q7 = qn7
end
Q4 = sqrt(5 + 2 * (sqrt(2))) * (Q7)
Q5 = (1 + (sqrt(2))) * Q7
Q6 = (sqrt(2)) * Q7
Q3 = Q4 + Q5
Q2 = 1 - Q3
Q8 = Q5
Q9 = Q3
println("Q9= ",Q9)
println("Q8= ",Q8)
println("Q7= ",Q7)
println("Q6= ",Q6)
println("Q5= ",Q5)
println("Q4= ",Q4)
println("Q3= ",Q3)
println("Q2= ",Q2)
println("Q1= ",Q1)
println("SEGUNDA PARTE")
f1 = 0
a = (4 * Q1) / (pi * 0.0000179 * 0.5)
i = 0;
x1 = 3
x2 = 0
fc = 1
i = 0
while fc > 0.0001 || fc < -0.0001
    global fx1 = 4 * log10(a * (x1^0.5)) - 0.4 - (1 / (x1^0.5))
    global fx2 = 4 * log10(a * (x2^0.5)) - 0.4 - (1 / (x2^0.5))
    global f1 = (x1 + x2) / 2
    global fc1 = 4 * log10(a * (f1^0.5)) - 0.4 - (1 / (f1^0.5))
    global i = i + 1
    global fc = fc1
    global r1 = fc1 * fx1
    global r2 = fc1 * fx2
    if r1 > 0
        global x1 = f1
    end
    if r2 > 0
        global x2 = f1
    end
end
f2 = 0
a = (4 * Q2) / (pi * 0.0000179 * 0.5)
i = 0;
x1 = 3
x2 = 0
fc = 1
i = 0
while fc > 0.0001 || fc < -0.0001
    global fx1 = 4 * log10(a * (x1^0.5)) - 0.4 - (1 / (x1^0.5))
    global fx2 = 4 * log10(a * (x2^0.5)) - 0.4 - (1 / (x2^0.5))
    global f2 = (x1 + x2) / 2
    global fc1 = 4 * log10(a * (f2^0.5)) - 0.4 - (1 / (f2^0.5))
    global i = i + 1
    global fc = fc1
    global r1 = fc1 * fx1
    global r2 = fc1 * fx2
    if r1 > 0
        global x1 = f2
    end
    if r2 > 0
        global x2 = f2
    end
end
f3 = 0
a = (4 * Q3) / (pi * 0.0000179 * 0.5)
i = 0;
x1 = 3
x2 = 0
fc = 1
i = 0
while fc > 0.0001 || fc < -0.0001
    global fx1 = 4 * log10(a * (x1^0.5)) - 0.4 - (1 / (x1^0.5))
    global fx2 = 4 * log10(a * (x2^0.5)) - 0.4 - (1 / (x2^0.5))
    global f3 = (x1 + x2) / 2
    global fc1 = 4 * log10(a * (f3^0.5)) - 0.4 - (1 / (f3^0.5))
    global i = i + 1
    global fc = fc1
    global r1 = fc1 * fx1
    global r2 = fc1 * fx2
    if r1 > 0
        global x1 = f3
    end
    if r2 > 0
        global x2 = f3
    end
end
f4 = 0
a = (4 * Q4) / (pi * 0.0000179 * 0.5)
i = 0;
x1 = 3
x2 = 0
fc = 1
i = 0
while fc > 0.0001 || fc < -0.0001
    global fx1 = 4 * log10(a * (x1^0.5)) - 0.4 - (1 / (x1^0.5))
    global fx2 = 4 * log10(a * (x2^0.5)) - 0.4 - (1 / (x2^0.5))
    global f4 = (x1 + x2) / 2
    global fc1 = 4 * log10(a * (f4^0.5)) - 0.4 - (1 / (f4^0.5))
    global i = i + 1
    global fc = fc1
    global r1 = fc1 * fx1
    global r2 = fc1 * fx2
    if r1 > 0
        global x1 = f4
    end
    if r2 > 0
        global x2 = f4
    end
end
f5 = 0
a = (4 * Q5) / (pi * 0.0000179 * 0.5)
i = 0;
x1 = 3
x2 = 0
fc = 1
i = 0
while fc > 0.0001 || fc < -0.0001
    global fx1 = 4 * log10(a * (x1^0.5)) - 0.4 - (1 / (x1^0.5))
    global fx2 = 4 * log10(a * (x2^0.5)) - 0.4 - (1 / (x2^0.5))
    global f5 = (x1 + x2) / 2
    global fc1 = 4 * log10(a * (f5^0.5)) - 0.4 - (1 / (f5^0.5))
    global i = i + 1
    global fc = fc1
    global r1 = fc1 * fx1
    global r2 = fc1 * fx2
    if r1 > 0
        global x1 = f5
    end
    if r2 > 0
        global x2 = f5
    end
end
f6 = 0
a = (4 * Q6) / (pi * 0.0000179 * 0.5)
i = 0;
x1 = 3
x2 = 0
fc = 1
i = 0
while fc > 0.0001 || fc < -0.0001
    global fx1 = 4 * log10(a * (x1^0.5)) - 0.4 - (1 / (x1^0.5))
    global fx2 = 4 * log10(a * (x2^0.5)) - 0.4 - (1 / (x2^0.5))
    global f6 = (x1 + x2) / 2
    global fc1 = 4 * log10(a * (f6^0.5)) - 0.4 - (1 / (f6^0.5))
    global i = i + 1
    global fc = fc1
    global r1 = fc1 * fx1
    global r2 = fc1 * fx2
    if r1 > 0
        global x1 = f6
    end
    if r2 > 0
        global x2 = f6
    end
end
f7 = 0
a = (4 * Q7) / (pi * 0.0000179 * 0.5)
i = 0;
x1 = 3
x2 = 0
fc = 1
i = 0
while fc > 0.0001 || fc < -0.0001
    global fx1 = 4 * log10(a * (x1^0.5)) - 0.4 - (1 / (x1^0.5))
    global fx2 = 4 * log10(a * (x2^0.5)) - 0.4 - (1 / (x2^0.5))
    global f7 = (x1 + x2) / 2
    global fc1 = 4 * log10(a * (f7^0.5)) - 0.4 - (1 / (f7^0.5))
    global i = i + 1
    global fc = fc1
    global r1 = fc1 * fx1
    global r2 = fc1 * fx2
    if r1 > 0
        global x1 = f7
    end
    if r2 > 0
        global x2 = f7
    end
end
f8 = 0
a = (4 * Q8) / (pi * 0.0000179 * 0.5)
i = 0
x1 = 3
x2 = 0
fc = 1
i = 0
while fc > 0.0001 || fc < -0.0001
    global fx1 = 4 * log10(a * (x1^0.5)) - 0.4 - (1 / (x1^0.5))
    global fx2 = 4 * log10(a * (x2^0.5)) - 0.4 - (1 / (x2^0.5))
    global f8 = (x1 + x2) / 2
    global fc1 = 4 * log10(a * (f8^0.5)) - 0.4 - (1 / (f8^0.5))
    global i = i + 1
    global fc = fc1
    global r1 = fc1 * fx1
    global r2 = fc1 * fx2
    if r1 > 0
        global x1 = f8
    end
    if r2 > 0
        global x2 = f8
    end
end
f9 = 0
a = (4 * Q9) / (pi * 0.0000179 * 0.5)
i = 0;
x1 = 3
x2 = 0
fc = 1
i = 0
while fc > 0.0001 || fc < -0.0001
    global fx1 = 4 * log10(a * (x1^0.5)) - 0.4 - (1 / (x1^0.5))
    global fx2 = 4 * log10(a * (x2^0.5)) - 0.4 - (1 / (x2^0.5))
    global f9 = (x1 + x2) / 2
    global fc1 = 4 * log10(a * (f9^0.5)) - 0.4 - (1 / (f9^0.5))
    global i = i + 1
    global fc = fc1
    global r1 = fc1 * fx1
    global r2 = fc1 * fx2
    if r1 > 0
        global x1 = f9
    end
    if r2 > 0
        global x2 = f9
    end
end
println("f1= ", f1)
println("f2= ", f2)
println("f3= ", f3)
println("f4= ", f4)
println("f5= ", f5)
println("f6= ", f6)
println("f7= ", f7)
println("f8= ", f8)
println("f9= ", f9)