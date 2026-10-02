c = input()
n1 = int(input())
n2 = int(input())

dirs = ["С", "В", "Ю", "З"]
i = dirs.index(c)

for n in (n1, n2):
    if n == 1:
        i = (i - 1) % 4
    elif n == -1:
        i = (i + 1) % 4
    else:
        i = (i + 2) % 4

print(dirs[i])
