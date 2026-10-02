import math

eps = float(input())

prev = 2.0
K = 1

while True:
    cur = 2 + 1 / prev
    K += 1

    if abs(cur - prev) < eps:
        break

    prev = cur

print(K, prev, cur)
