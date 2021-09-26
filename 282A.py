t = int(input())
iniValue = 0
for i in range(0, t):
    operation = input().split("X")
    for items in operation:
        if(items != ''):
            if(items == '++'):
                iniValue = iniValue + 1
            elif(items == '--'):
                iniValue = iniValue - 1
print(iniValue)