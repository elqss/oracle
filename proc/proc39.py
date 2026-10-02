import math

def power1(a, b):
    if a <= 0:
        return 0
    return math.exp(b * math.log(a))

def power2(a, n):
    if n == 0:
        return 1

    p = 1.0
    for i in range(abs(n)):
        p *= a

    if n < 0:
        p = 1 / p

    return p

def power3(a, b):
    if b == int(b):
        return power2(a, int(b))
    return power1(a, b)

p = float(input())
a = float(input())
b = float(input())
c = float(input())

print(power3(a, p))
print(power3(b, p))
print(power3(c, p))
