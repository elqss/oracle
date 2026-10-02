def fact2(n):
    p = 1.0
    i = 2 if n % 2 == 0 else 1
    while i <= n:
        p *= i
        i += 2
    return p

for i in range(5):
    n = int(input())
    print(fact2(n))
