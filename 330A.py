r, c = map(int, input().split(" "))
soDau = []
 
for i in range (0, r):
    s = input()
    row = []
    for j in range (0, c):
        if s[j] == "S":
            row.append(1)
        else:
            row.append(0)
    soDau.append(row)
soHangToanDau = 0
soDauTemp1 = soDau.copy()
for dau in soDauTemp1:
    if len(set(dau)) == 1 and dau[0] == 0:
        soHangToanDau += 1
        soDau.remove(dau)
if len(soDau) == 0:
    print(r * c)
else:
    soDautemp2 = soDau.copy()
    thuTuDau = []
    for dau in soDautemp2:
        temp = []
        for d in range(0, len(dau)):
            if dau[d] == 1:
                temp.append(d)
        thuTuDau.append(temp)

    t = ""
    for vt in thuTuDau:
        for v in vt:
            t += str(v) + " "
    soCotChuaDau = len(set(t[0: -1].split(" ")))
    soCotKhongDau = c - soCotChuaDau

    print("soCotChuaDau: ", soCotChuaDau)
    print("soCotKhongDau: ", soCotKhongDau)

    print("soHangToanDau: ", soHangToanDau)
    print("soCotKhongDau: ", soCotKhongDau)
    print(soHangToanDau * c + soCotKhongDau * (r - soHangToanDau))