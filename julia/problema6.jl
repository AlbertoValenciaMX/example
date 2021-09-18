# a: etilbenceno
# b: tolueno
# Datos
pa = 250 # mmHg
pb = 343 # mmhg
# parámetros Ley de Antoine
Aa = 6.95719; Ba = 1424.255; Ca = 213.21
Ab = 6.95464; Bb = 1344.8; Cb = 219.48
PT = pa + pb
println("La presión total es: ",PT, " mmHg")
ya = pa / PT
yb = pb / PT
println("La fracción molar del etilbenceno es: ",ya)
println("La fracción molar del tolueno es: ",yb)
Pa0 = pa / ya
Pb0 = pb / yb
println("La presión de saturación del etilbenceno es: ",Pa0)
println("La presión de saturación del tolueno es: ",Pb0)
# Para calcular la temperatura de cada compuesto podemos usar la ecuación de Antonie despejando la T
# T=(-B-C*log(Pi0)+AC)/(log(Pi0)-A)
Ta = (-Ba - Ca * log(Pa0) + Aa * Ca) / (log(Pa0) - Aa)
Tb = (-Bb - Cb * log(Pb0) + Ab * Cb) / (log(Pb0) - Ab)
println("La Temperatura del etilbenceno es: ",Ta, " ºC")
println("La Temperatura del tolueno es: ",Tb, " ºC")