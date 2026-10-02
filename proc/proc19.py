def ring_s(r1, r2):
    return 3.14 * (r1 * r1 - r2 * r2)

for i in range(3):
    r1 = float(input())
    r2 = float(input())
    print(ring_s(r1, r2))
