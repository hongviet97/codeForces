n = str(input())

lstN = []
lenLstN = 0
for i in range(0, len(n)):
    if n[i] == "Q" or n[i] == "A":
        lstN += n[i]
        lenLstN += 1
print(lstN)
print(lenLstN)
strings = "".join(str(y) for y in lstN)
print(strings)

countA = lstN.count("A")
print("soA: ", countA)

soQAQ = 0
for x in range(0, lenLstN):
    if strings[x] == "A":
        stringstemp = strings.split("A", 1)
        soQTrai = stringstemp[0].count("Q")
        soQphai = stringstemp[1].count("Q")
        stringsSau = strings.replace("A", "-", 1)
        strings = stringsSau
        soQAQ += soQphai * soQTrai
        print(stringstemp)
        print(soQTrai)
        print(soQphai)
        print(stringsSau)
        print(strings)
        print(soQAQ)
        print("__________________________")
print(soQAQ)