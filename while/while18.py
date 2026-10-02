N = int(input())

K = 0
S = 0

while N > 0:
    S += N % 10
    K += 1
    N //= 10

print(K, S)
