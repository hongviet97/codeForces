i = 0

n, k = map(int, input().split(" "))
scores = list(map(float, input().split(" ")))
print(scores)
for x in range(0, n):
    if scores[k-1] == 0 and scores[x] ==0:
        i = i + 0
    elif scores[k-1] <= scores[x]:
        i = i + 1
print(i)

# ip = input().split(" ")
# n = int(ip[0])
# k = int(ip[-1])
# print(k)
# diem = input().split(" ")
# print("danh sach diem", diem)
# couter = 0
# print("vi tri cua k", diem[k - 1])
# for i in range(0 ,n):
#     print(diem[i])
#     print(diem[k - 1])
#     if(int(diem[i]) == 0):
#         couter = couter + 0
#     elif(int(diem[i]) >= int(diem[k - 1])):
#         couter += 1
#     print("-------------------------------------")
# print(couter)
