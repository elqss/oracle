X = float(input())
N = int(input())

S = 0.0
power = X

for i in range(N + 1):
    S += ((-1) ** i) * power / (2 * i + 1)
    power *= X * X

print(S)
