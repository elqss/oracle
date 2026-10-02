a = float(input())
b = float(input())
c = float(input())
db = abs(b - a)
dc = abs(c - a)
if db < dc:
    print(b, db)
else:
    print(c, dc)
