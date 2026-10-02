def ln1(x, e):
    s = 0.0
    term = x
    n = 1

    while abs(term) > e:
        s += term
        n += 1
        term = (-1) ** (n - 1) * x ** n / n

    return s

x = float(input())

for i in range(6):
    e = float(input())
    print(ln1(x, e))
