def deSum(r):    
    lenBanDau = 0
    tempSum = 0
    check = True
    i = 1
    while(check):
        lenBanDau += 1
        tempSum += i
        if(tempSum == r):
            check = False
        i += 1
    return lenBanDau

chuoiGoc = "baabbb"

# n =int(input())
# t = input()

# doDaiChuoiGoc = deSum(n)
# chuoiBanDau = ""
# for i in range(1, doDaiChuoiGoc + 1):
#     chuoiTemp = t[0:i]
#     # print("chuoiTemp: ", chuoiTemp)
#     chuoiSauKhiCat = t[i::]
#     t = chuoiSauKhiCat
#     # print("chuoiSauKhiCat: ", t)
#     chuoiBanDau += chuoiTemp[0]
# print("chuoiBanDau: ", chuoiBanDau)