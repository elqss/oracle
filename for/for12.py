N = int(input())

P = 1.0

for i in range(N):
    P *= 1.1 + i / 10

print(P)
