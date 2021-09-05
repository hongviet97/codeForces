# def uscln(a, b):
#     if (b == 0):
#         return a
#     return uscln(b, a % b)
# def bscnn(a, b):
#     return int((a * b) / uscln(a, b))

t = int(input())
for i in range(0, t):
    x = int(input())
    print(1, end=" ")
    print(x - 1)