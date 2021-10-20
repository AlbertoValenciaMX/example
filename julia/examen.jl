using PyPlot

v0=200 #l
vf=0
rho=1 #kg/l
v1=2
v2=3
v3=6
x1=0.20
x2=0.10
V=zeros(201)
X=zeros(201) tiempo=zeros(201) V[1]=v0
X[1]=.25
for i=2:201
global V[i]=V[i-1]-1
global X[i]=((v1*x1)+(v2*x2)+(rho*V[i-1]*X[i-1]))/(rho*V[i]+v3) global tiempo[i]=i-1
end
println("concentracion final es:",X)
figure(1)

plot(tiempo,X,label=" Discretizando") ylabel("Concentración") xlabel("tiempo")

legend(bbox_to_anchor=(0,1), loc=2) grid("on")

figure(2) plot(tiempo,V) ylabel("Volumen") xlabel("tiempo")
