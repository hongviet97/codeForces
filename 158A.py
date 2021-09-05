ip = input().split(" ")
n = int(ip[0])
k = int(ip[-1])
print(k)
diem = input().split(" ")
print("danh sach diem", diem)
couter = 0
print("vi tri cua k", diem[k - 1])
for i in range(0 ,n):
    print(diem[i])
    print(diem[k - 1])
    if(int(diem[i]) == 0):
        couter = couter + 0
    elif(int(diem[i]) >= int(diem[k - 1])):
        couter += 1
    print("-------------------------------------")
print(couter)