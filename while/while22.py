N = int(input())

K = 2
simple = True

while K * K <= N:
    if N % K == 0:
        simple = False
        break
    K += 1

if simple:
    print("TRUE")
else:
    print("FALSE")
