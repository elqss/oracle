a = float(input())
b = float(input())
c = float(input())
if (a < b < c) or (a > b > c):
    a *= 2
    b *= 2
    c *= 2
else:
    a = -a
    b = -b
    c = -c
print(a, b, c)
