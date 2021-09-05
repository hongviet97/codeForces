n = int(input())
height = list(map(int, input().split(" ")))
data = []
minusHeight = []
for i in range(0, n):
    tempList = []
    if i == n - 1:
        tempList.append(height[i])
        tempList.append(height[0])
        tempList.append(abs(height[i] - height[0]))
        minusHeight.append(abs(height[i] - height[0]))
        data.append(tempList)
    else:
        tempList.append(height[i])
        tempList.append(height[i + 1])
        tempList.append(abs(height[i] - height[i + 1]))
        minusHeight.append(abs(height[i] - height[i + 1]))
        data.append(tempList)
minHeight = min(minusHeight)
minPair = []
for d in data:
    if d[2] == minHeight:
        minPair = d.copy()
        break

print("minPair: ", minPair)

fakeHeight1 = []
fakeHeight2 = []

index = height.index(minPair[0]) + 1
for h in range(0, len(height)):
    if height[h] == minPair[0]:
        fakeHeight1.append(h)
print(fakeHeight1)
 
for h in range(0, len(height)):
    if height[h] == minPair[1]:
        fakeHeight2.append(h)
print(fakeHeight2)
 
lstFinal = fakeHeight1 + fakeHeight2
lstFinal.sort()
# print(lstFinal)
 
check = 0
for h in range(0, len(lstFinal)):
    if(h == len(lstFinal) - 1):
        break
    else:
        if lstFinal[h] + 1 == lstFinal[h + 1]:
            print(lstFinal[h] + 1, lstFinal[h + 1] + 1)
            check = 1
            break
if check == 0:
    print(1, n)