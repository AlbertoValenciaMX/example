#Problema 2
T=[79.7 105.8 120.0 141.8 178.5 197.3]
P=[5 20 40 100 400 760.0]

using PyPlot

scatter(T,P,color="red",label="datos")
xlabel("T - temperatura")
ylabel("P - presion ")
Sxy=0
Sx=0
Sy=0
Sx2=0
Sy2=0
n=6

for i=1:n
    global Sxy=Sxy+(T[i]*P[i])
    global Sx=Sx+T[i]
    global Sy=Sy+P[i]
    global Sx2=Sx2+(T[i]^2)
    global Sy2=Sy2+(P[i]^2)
end

    beta1=((n*Sxy)-(Sx*Sy))/((n*Sx2)-(Sx^2))
    xp=Sx/n
    yp=Sy/n
    beta0=yp-(beta1*xp)

    YN=zeros(n)

    for i=1:n
        global YN[i]=(beta1*T[i])+beta0
    end

    plot(transpose(T),YN,color="purple",label="lineal")

println("\n ###########################################################")
    println("\n \n la función es y = ",beta1," x + ",beta0)
r=((n*Sxy)-(Sx*Sy))/(sqrt(n*Sx2-(Sx^2))*sqrt(n*Sy2-(Sy^2)))
    println("el factor de correlación (r) es de ",r)

Tl=zeros(n)
Pl=zeros(n)

for i=1:n
    Tl[i]=log(T[i])
    Pl[i]=log(P[i])
end

Sxy=0
Sx=0
Sy=0
Sx2=0
Sy2=0
n=6

for i=1:n
    global Sxy=Sxy+(Tl[i]*Pl[i])
    global Sx=Sx+Tl[i]
    global Sy=Sy+Pl[i]
    global Sx2=Sx2+(Tl[i]^2)
    global Sy2=Sy2+(Pl[i]^2)
end

    beta1=((n*Sxy)-(Sx*Sy))/((n*Sx2)-(Sx^2))
    xp=Sx/n
    yp=Sy/n
    beta0=yp-(beta1*xp)

    YN=zeros(n)

    for i=1:n
        global YN[i]=exp(beta0)*(T[i]^beta1)
    end

    plot(transpose(T),YN,color="green",label="potencia")
    legend(bbox_to_anchor=(0.1,1), loc=2)
    grid("on")

    println("\n ###########")
        println("\n la función es y = ",exp(beta0)," * x ^ ",beta1)
    r=((n*Sxy)-(Sx*Sy))/(sqrt(n*Sx2-(Sx^2))*sqrt(n*Sy2-(Sy^2)))
        println("el factor de correlación (r) es de ",r)

plt.show()