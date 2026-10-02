X = float(input())
N = int(input())

fact = 1.0
power = 1.0
S = 1.0

for i in range(1, N + 1):
    fact *= (2 * i - 1) * (2 * i)
    power *= X * X
    if i % 2 == 1:
        S -= power / fact
    else:
        S += power / fact

print(S)
