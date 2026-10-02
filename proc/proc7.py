def invert_digits(k):
    result = 0
    while k > 0:
        result = result * 10 + k % 10
        k //= 10
    return result

for i in range(5):
    k = int(input())
    print(invert_digits(k))
