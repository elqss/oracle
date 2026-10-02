import math

n = int(input())
v = float(input())

if n == 1:
    r = v
elif n == 2:
    r = v / 2
elif n == 3:
    r = v / (2 * 3.14)
else:
    r = math.sqrt(v / 3.14)

print(r, 2 * r, 2 * 3.14 * r, 3.14 * r * r)
