t = int(input())
for i in range(0, t):
    n = list(map(int, input().split()))
    for i in range(0, n + 1):
        if n[i] % 4 == 0:
            print("YES")
        else:
            print("NO")