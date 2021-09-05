n = int(input())
counter = 0
for i in range (0, n):
    x = input()
    # prin5t(x)
    if x.count("1") >= 2:
        counter += 1
print(counter)