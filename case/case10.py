c = input()
n = int(input())

dirs = ["С", "В", "Ю", "З"]
i = dirs.index(c)

if n == 1:
    i = (i - 1) % 4
elif n == -1:
    i = (i + 1) % 4

print(dirs[i])
