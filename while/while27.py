N = int(input())

a = 1
b = 1
K = 2

while b < N:
    a, b = b, a + b
    K += 1

print(K)
