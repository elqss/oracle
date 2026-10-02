import math

x = float(input())
if x < 0:
    f = 0
else:
    n = int(x)
    if n % 2 == 0:
        f = 1
    else:
        f = -1
print(f)
