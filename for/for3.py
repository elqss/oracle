A = int(input())
B = int(input())

N = 0

for i in range(B - 1, A, -1):
    print(i)
    N += 1

print(N)
