import math

def power1(a, b):
    if a <= 0:
        return 0
    return math.exp(b * math.log(a))

p = float(input())
a = float(input())
b = float(input())
c = float(input())

print(power1(a, p))
print(power1(b, p))
print(power1(c, p))
