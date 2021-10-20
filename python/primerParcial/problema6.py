import math
# a: etilbenceno
# b: tolueno
# Datos
pa = 250 # mmHg
pb = 343 # mmhg
# parámetros Ley de Antoine
Aa = 6.95719; Ba = 1424.255; Ca = 213.21
Ab = 6.95464; Bb = 1344.8; Cb = 219.48
PT = pa + pb
print("La presión total es: ",PT, " mmHg")
ya = pa / PT
yb = pb / PT
print("La fracción molar del etilbenceno es: ",ya)
print("La fracción molar del tolueno es: ",yb)
Pa0 = pa / ya
Pb0 = pb / yb
print("La presión de saturación del etilbenceno es: ",Pa0)
print("La presión de saturación del tolueno es: ",Pb0)
# Para calcular la temperatura de cada compuesto podemos usar la ecuación de Antonie despejando la T
# T=(-B-C*log(Pi0)+AC)/(log(Pi0)-A)
Ta = (-Ba - Ca * math.log(Pa0) + Aa * Ca) / (math.log(Pa0) - Aa)
Tb = (-Bb - Cb * math.log(Pb0) + Ab * Cb) / (math.log(Pb0) - Ab)
print("La Temperatura del etilbenceno es: ",Ta, " ºC")
print("La Temperatura del tolueno es: ",Tb, " ºC")