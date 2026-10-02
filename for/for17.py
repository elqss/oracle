A = float(input())
N = int(input())

S = 1.0
P = 1.0

for i in range(1, N + 1):
    P *= A
    S += P

print(S)
