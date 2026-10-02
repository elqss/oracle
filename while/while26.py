N = int(input())

a = 1
b = 1

while b < N:
    a, b = b, a + b

print(a, a + b)
