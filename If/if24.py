import math

x = float(input())
if x > 0:
    f = 2 * math.sin(x)
else:
    f = 6 - x
print(f)
