t = int(input())
for i in range(0, t):
    w, h, n = map(int, input().split())
    count = 1
    while w % 2 == 0:
        w = w / 2
        count = count * 2
    print("countSau = ", count)
    while h % 2 == 0:
        h = h / 2
        count = count * 2
    print("countSau = ", count)
    if count >= n:
        print("YES")
    else:
        print("NO")