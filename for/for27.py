X = float(input())
N = int(input())

S = X
power = X
odd = 1
even = 2

for i in range(1, N + 1):
    power *= X * X
    odd *= 2 * i - 1
    even *= 2 * i
    term = odd * power / (even * (2 * i + 1))
    S += term

print(S)
