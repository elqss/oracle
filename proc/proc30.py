def digit_n(k, n):
    for i in range(n - 1):
        k //= 10
    if k == 0:
        return -1
    return k % 10

n = int(input())

for i in range(5):
    k = int(input())
    print(digit_n(k, n))
