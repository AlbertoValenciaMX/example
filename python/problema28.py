import numpy as np

pm = [78.11,92.14,104.15,106.16]
nE = 70
xE = [0.20,0.40,0.25,0.15]
mE = np.zeros(4)
mTE = 0
for i in range(0,4):
    mE[i] = (nE * xE[i]) * pm[i]
    mTE = mTE + mE[i]

print("Composición inicial= ",mE)
print("Flujo másico inicial= ",mTE)
Acoef = [[0.35, 0.16, 0.21, 0.01], [0.54, 0.42, 0.54, 0.1], [0.04, 0.24, 0.1, 0.65], [0.07, 0.18, 0.15, 0.24]]
Bflu = [[mE[1]], [mE[2]], [mE[3]], [mE[4]]]
FsF = np.dot(np.linalg.inv(Acoef), Bflu)
print("D1,B1,D2,B2:"+str(FsF))
FsE = [FsF[1] + FsF[2],FsF[3] + FsF[4]]
print("D, B:"+str(FsE))
xD = np.zeros(4)
xB = np.zeros(4)
xD1 = [0.35, 0.54, 0.04, 0.07]
xB1 = [0.16, 0.42, 0.24, 0.18]
xD2 = [0.21, 0.54, 0.10, 0.15]
xB2 = [0.01, 0.1, 0.65, 0.24]
for i in range(0,4):
    xD[i] = ((FsF[1] * xD1[i] + FsF[2] * xB1[i])) / FsE[1]
    xB[i] = ((FsF[3] * xD2[i] + FsF[4] * xB2[i])) / FsE[2]

print("Fracción en D: "+ str(xD))
print("Fracción en B: "+ str(xB))
