n, k = map(int, input().split(" "))
Ranks = list(map(int, input().split(" ")))
distincRanks = list(set(Ranks))
# print(Ranks)
# print(distincRanks)
if len(distincRanks) < k:
    print("NO")
else:
    print("YES")
    for i in range(k):
        print((Ranks.index(distincRanks[i])) + 1, end=" ") 