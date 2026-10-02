X = float(input())
N = int(input())

S = 1.0
power = 1.0
fact = 1.0

for i in range(1, N + 1):
    power *= X
    fact *= 2 * i
    term = power / fact

    if i % 2 == 1:
        S += term
    else:
        S -= term

print(S)
