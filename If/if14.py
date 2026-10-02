a = float(input())
b = float(input())
c = float(input())
if a < b and a < c:
    mn = a
elif b < c:
    mn = b
else:
    mn = c
if a > b and a > c:
    mx = a
elif b > c:
    mx = b
else:
    mx = c
print(mn, mx)
