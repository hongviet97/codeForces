t = int(input())
for i in range (0, t):
    n = int(input())
    lst1 = list(map(int, input().split(" ")))
    if n == 1:
        print(lst1[0])
    elif n == 2:
        print(lst1[0], end=" ") 
        print(lst1[1])
    elif n == 3:
        print(lst1[0], end=" ")
        print(lst1[2], end=" ")
        print(lst1[1])
    else:
        chuoi = ""
        chuoi1 = ""
        for x in range (0, int(n/2)):
            chuoi += str(lst1[x]) + " " + str(lst1[-(x+1)]) + " "
            if n % 2 == 0:
                chuoi1 = chuoi
            elif n % 2 == 1:
                chuoi1 = chuoi + str(lst1[int(n/2)])
        print(chuoi1)