X = float(input())
N = int(input())

fact = 1.0
power = 1.0
S = 1.0

for i in range(1, N + 1):
    power *= X
    fact *= i
    S += power / fact

print(S)
