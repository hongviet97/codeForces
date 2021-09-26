n = input()
string = input()
string = string.lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
count = 0
for letter in alphabet:
    if letter not in string:
        count += 1
if count > 0:
    print("NO")
else:
    print("YES")
