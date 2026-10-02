def cos1(x, e):
    s = 0.0
    term = 1.0
    n = 2

    while abs(term) > e:
        s += term
        term *= -x * x / ((n - 1) * n)
        n += 2

    return s

x = float(input())

for i in range(6):
    e = float(input())
    print(cos1(x, e))
