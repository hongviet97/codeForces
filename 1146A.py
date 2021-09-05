s = input()
soA = s.count("a")
if soA > len(s) / 2:
    print(len(s))
else:
    print(soA * 2 - 1)