def power4(x, a, e):
    s = 1.0
    term = 1.0
    n = 1

    while True:
        term *= (a - n + 1) * x / n
        if abs(term) <= e:
            break
        s += term
        n += 1

    return s

x = float(input())
a = float(input())

for i in range(6):
    e = float(input())
    print(power4(x, a, e))
