N = int(input())
K = int(input())

Q = 0
R = N

while R >= K:
    R -= K
    Q += 1

print(Q, R)
