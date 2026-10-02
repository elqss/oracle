def add_left_digit(d, k):
    p = 1
    while p <= k:
        p *= 10
    return d * p + k

k = int(input())
d1 = int(input())
d2 = int(input())

k = add_left_digit(d1, k)
print(k)
k = add_left_digit(d2, k)
print(k)
