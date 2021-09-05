n = int(input())
lstPlanes = list(map(int, input().split()))
# lstPlanes = [lstPlanes[i] - 1 for i in range(n)]
# print(lstPlanes)

# Hai list chứa index và item tương ứng
lstInd = []
lstItem = []
a = ""
# Nhặt từ lstPlanes
for ind, item in enumerate(lstPlanes):
#     lstInd.append(ind)
#     lstItem.append(item)
# print(lstItem)
# print(lstInd)
    print(ind, item)



# n = int(input())
# check = 0
# lstPlanes = list(map(int, input().split()))
# print(lstPlanes)
# lstPlanes = [lstPlanes[i]-1 for i in range(n)]
# print(lstPlanes)

# lstTemp =[]

# for i in range(n):
#     if lstPlanes[lstPlanes[lstPlanes[i]]] == i:
#         # print(lstPlanes[lstPlanes[lstPlanes[i]]], end=" ")
#         print("YES")
#     else:
#         print("NO")




# for i in range(n):
#     if lstPlanes[lstPlanes[lstPlanes[i]]] == i: 
#         check = 1
#         print("i = ", i)
#         print(lstPlanes[lstPlanes[lstPlanes[i]]])
#         print("----------------------")
# print("YES" if check else "NO")