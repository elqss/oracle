d = int(input())
m = int(input())

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d -= 1
if d == 0:
    m -= 1
    if m == 0:
        m = 12
    d = days[m - 1]
print(d, m)
