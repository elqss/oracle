def is_palindrom(k):
    old = k
    new = 0

    while k > 0:
        new = new * 10 + k % 10
        k //= 10

    return old == new

count = 0
for i in range(10):
    k = int(input())
    if is_palindrom(k):
        count += 1

print(count)
