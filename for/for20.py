N = int(input())

fact = 1.0
S = 0.0

for i in range(1, N + 1):
    fact *= i
    S += fact

print(S)
