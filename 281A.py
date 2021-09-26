# def vietHoaChuDau(string):
#     return " ".join(letter[0].upper() + letter[1:] for letter in string.split(" "))
# word = vietHoaChuDau(input())
# print(word)

word = input()
word = " ".join(letter[0].upper() + letter[1:] for letter in word.split(" "))
print(word)