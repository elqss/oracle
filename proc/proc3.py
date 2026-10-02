import math

def mean(x, y):
    a = (x + y) / 2
    g = math.sqrt(x * y)
    return a, g

a = float(input())
b = float(input())
c = float(input())
d = float(input())

print(mean(a, b))
print(mean(a, c))
print(mean(a, d))
