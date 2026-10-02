a = float(input())
b = float(input())
c = float(input())
if a < b:
    mn = a
    mid = b
else:
    mn = b
    mid = a
if c < mn:
    mn = c
elif c > mid:
    pass
else:
    mid = c
if a > b:
    mx = a
else:
    mx = b
if c > mx:
    mx = c
print(mid + mx)
