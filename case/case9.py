d = int(input())
m = int(input())

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d += 1
if d > days[m - 1]:
    d = 1
    m += 1
    if m > 12:
        m = 1
print(d, m)
