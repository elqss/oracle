N = int(input())

a = 1
b = 1

while b < N:
    a, b = b, a + b

if b == N:
    print("TRUE")
else:
    print("FALSE")
