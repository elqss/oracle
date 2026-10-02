N = int(input())

S = 0

for i in range(1, N + 1):
    if i % 2 == 1:
        S += i / 10
    else:
        S -= i / 10

print(S)
