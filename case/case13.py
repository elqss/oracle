import math

n = int(input())
v = float(input())

if n == 1:
    a = v
elif n == 2:
    a = v * math.sqrt(2)
elif n == 3:
    a = 2 * v
else:
    a = math.sqrt(2 * v)

c = a * math.sqrt(2)
h = c / 2
s = c * h / 2

print(a, c, h, s)
