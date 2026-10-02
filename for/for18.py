A = float(input())
N = int(input())

S = 1.0
P = 1.0

for i in range(1, N + 1):
    P *= A
    if i % 2 == 1:
        S -= P
    else:
        S += P

print(S)
