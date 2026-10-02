def exp1(x, e):
    s = 1.0
    term = 1.0
    n = 1

    while True:
        term *= x / n
        if abs(term) <= e:
            break
        s += term
        n += 1

    return s

x = float(input())

for i in range(6):
    e = float(input())
    print(exp1(x, e))
