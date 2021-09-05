n = int(input())
lstPacks = list(map(int, input().split()))
soBongCuaGri = 0

for ele in range(0, len(lstPacks[0:-1])):
    if len(lstPacks) <= 2 and lstPacks[0] == lstPacks[1]:
        print("-1")
    else:
        soBongCuaGri = soBongCuaGri + lstPacks[ele]
        print(ele, end=" ")
# print("Tổng số bóng = ", soBongCuaGri)

