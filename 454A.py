n = int(input())
center = int((n - 1) / 2)
soLuongD = 1
side = ""
for i in range(0, n):
    side = "*" * int((n - soLuongD) / 2)
    diamond = "D" * soLuongD
    line = side + diamond + side
    print(line)
    if i < center:
        soLuongD += 2
    else:
        soLuongD -= 2