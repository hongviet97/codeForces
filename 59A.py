chuoiBanDau = str(input())
countLow = 0
countUp = 0
for i in range (0, len(chuoiBanDau)):
    if chuoiBanDau[i].islower():
        countLow += 1
    else:
        countUp += 1
if countUp > countLow:
    print(chuoiBanDau.upper())
else:
    print(chuoiBanDau.lower())