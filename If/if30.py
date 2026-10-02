a = int(input())
if a < 10:
    digits = "однозначное"
elif a < 100:
    digits = "двузначное"
else:
    digits = "трехзначное"

if a % 2 == 0:
    kind = "четное"
else:
    kind = "нечетное"

print(kind, digits, "число")
