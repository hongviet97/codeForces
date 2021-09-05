t = int(input())
for i in range(0, t):
    n, x = map(int, input().split())
    if n <= 2:
        print("1")
    elif 3 <= n <= (x + 2):
        print("2")
    else:
        for a in range(0, 1001):
            if (a + 1) * x + 3 <= n <= (a + 2) * x + 2:
                print(a + 3)