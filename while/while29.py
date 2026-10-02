eps = float(input())

a = 1.0
b = 2.0
K = 2

while True:
    c = (a + 2 * b) / 3
    K += 1

    if abs(c - b) < eps:
        break

    a = b
    b = c

print(K, b, c)
