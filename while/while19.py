N = int(input())

R = 0

while N > 0:
    R = R * 10 + N % 10
    N //= 10

print(R)
