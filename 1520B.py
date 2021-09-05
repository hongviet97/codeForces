t = int(input())
for i in range(0, t):
    n = input()
    if 0 <= int(n) <= 9:
        print(n)
    elif int(n) > 9:
        soChuSo = len(n)
        ordinaryNearest = len(n) * n[0]
        print(int(n))
        print(int(ordinaryNearest))
        if int(n) < int(ordinaryNearest):
            print((((soChuSo-1) * 9) + int(n[0])) - 1)
        else:
            print(((soChuSo-1) * 9) + int(n[0]))