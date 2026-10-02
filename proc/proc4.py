import math

def triangle_ps(a):
    p = 3 * a
    s = a * a * math.sqrt(3) / 4
    return p, s

for i in range(3):
    a = float(input())
    print(triangle_ps(a))
