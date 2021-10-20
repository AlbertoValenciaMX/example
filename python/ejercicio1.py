xF = 0.10
xrp = 0.0075
mp = 4850
xrA = 0.05
xB = 0.01

#Balance global de R
mAi = (xrp*mp)/xrA
print("flujo másico inicial del intermediario A es ", mAi, " en kg de A/hora")

#Balance Global de todo el sistema
mBi = mp-mAi
print("flujo másico inicial de la otra corriente es corriente es ", mBi, " en kg de B/hora")

#Balance donde va R
F = (xrp*mp)/xF
print("La alimentación F para el reactor es ",F, " en kg de A/hora")