def fact(n):
    p = 1.0
    for i in range(1, n + 1):
        p *= i
    return p

for i in range(5):
    n = int(input())
    print(fact(n))
