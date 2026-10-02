def is_prime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

count = 0
for i in range(10):
    n = int(input())
    if is_prime(n):
        count += 1

print(count)
