def minmax(x, y):
    if x > y:
        x, y = y, x
    return x, y

a = float(input())
b = float(input())
c = float(input())
d = float(input())

a, b = minmax(a, b)
c, d = minmax(c, d)
a, c = minmax(a, c)
b, d = minmax(b, d)

print(a, d)
