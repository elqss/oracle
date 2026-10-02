import math

n = int(input())
v = float(input())

if n == 1:
    a = v
elif n == 2:
    a = v * 2 * math.sqrt(3)
elif n == 3:
    a = v * 3 * math.sqrt(3)
else:
    a = math.sqrt(4 * v / math.sqrt(3))

r1 = a * math.sqrt(3) / 6
r2 = 2 * r1
s = a * a * math.sqrt(3) / 4

print(a, r1, r2, s)
