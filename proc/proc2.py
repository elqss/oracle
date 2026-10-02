def power_a234(a):
    b = a * a
    c = b * a
    d = c * a
    return b, c, d

for i in range(5):
    a = float(input())
    print(power_a234(a))
