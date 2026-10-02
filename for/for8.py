A = int(input())
B = int(input())

P = 1

for i in range(A, B + 1):
    P *= i

print(P)
