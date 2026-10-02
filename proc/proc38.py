def power2(a, n):
    if n == 0:
        return 1

    p = 1.0
    for i in range(abs(n)):
        p *= a

    if n < 0:
        p = 1 / p

    return p

a = float(input())
k = int(input())
l = int(input())
m = int(input())

print(power2(a, k))
print(power2(a, l))
print(power2(a, m))
