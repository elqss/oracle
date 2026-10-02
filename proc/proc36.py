def fib(n):
    a = 1
    b = 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return a if n == 1 else b

for i in range(5):
    n = int(input())
    print(fib(n))
