X = float(input())
N = int(input())

S = 0.0
power = X

for i in range(1, N + 1):
    S += ((-1) ** (i - 1)) * power / i
    power *= X

print(S)
