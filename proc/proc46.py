def nod2(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(nod2(a, b))
print(nod2(a, c))
print(nod2(a, d))
