xF = 0.10
xrp = 0.0075
mp = 4850
xrA = 0.05
xB = 0.01

#Balance global de R
mAi = (xrp*mp)/xrA
println("flujo másico inicial del intermediario A es ", mAi, " en kg de A/hora")

#Balance Global de todo el sistema
global mBi = mp-mAi
println("flujo másico inicial de la otra corriente es corriente es ", mBi, " en kg de B/hora")

#Balance donde va R
global F = (xrp*mp)/xF
println("La alimentación F para el reactor es ",F, " en kg de A/hora")
