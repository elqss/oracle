def digit_count_sum(k):
    count = 0
    s = 0
    while k > 0:
        s += k % 10
        count += 1
        k //= 10
    return count, s

for i in range(5):
    k = int(input())
    print(digit_count_sum(k))
