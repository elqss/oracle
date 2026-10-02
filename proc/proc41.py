def sin1(x, e):
    s = 0.0
    term = x
    n = 1

    while abs(term) > e:
        s += term
        n += 2
        term *= -x * x / ((n - 1) * n)

    return s

x = float(input())

for i in range(6):
    e = float(input())
    print(sin1(x, e))
