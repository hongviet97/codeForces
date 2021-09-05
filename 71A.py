n = int(input())
 
for i in range(0 , n):
    x = str(input())
    l = len(x)
    if l>10:
        print(x[0], end="")
        print(l-2, end="")
        print(x[-1])
    else:
        print(x)