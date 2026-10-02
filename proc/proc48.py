def nod2(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def nok2(a, b):
    return a * (b // nod2(a, b))

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(nok2(a, b))
print(nok2(a, c))
print(nok2(a, d))
