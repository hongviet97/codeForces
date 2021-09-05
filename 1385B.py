def sorting(input):
    lstInput = input.split(" ")
    output = []
    for x in lstInput:
        if x not in output:
            output.append(x)
    print(" ".join(x for x in output))
t = int(input())
for i in range(0, t):
    n = int(input())
    lstPx2 = str(input())
    sorting(lstPx2)