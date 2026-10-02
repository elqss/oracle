N = int(input())

P = 1.0

while N > 0:
    P *= N
    N -= 2

print(P)
