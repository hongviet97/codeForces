n = input()
string = input()
string = string.lower()
countN = 0
countZ = 0
result = ""
for i in string:
    if i == "n":
        result = result + "1 "
    
for y in string: 
    if y == "z":
        result = result + "0 " 

print(result)
