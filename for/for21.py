N = int(input())

fact = 1.0
S = 1.0

for i in range(1, N + 1):
    fact *= i
    S += 1 / fact

print(S)
