import math

def is_square(k):
    r = math.isqrt(k)
    return r * r == k

count = 0
for i in range(10):
    k = int(input())
    if is_square(k):
        count += 1

print(count)
