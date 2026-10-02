def nod2(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def frac1(a, b):
    if b < 0:
        a = -a
        b = -b

    g = nod2(abs(a), b)
    return a // g, b // g

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())

p, q = frac1(a * d + c * b, b * d)
print(p, q)

p, q = frac1(a * f + e * b, b * f)
print(p, q)

p, q = frac1(a * h + g * b, b * h)
print(p, q)
