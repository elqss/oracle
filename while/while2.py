A = float(input())
B = float(input())

K = 0

while A >= B:
    A -= B
    K += 1

print(K)
