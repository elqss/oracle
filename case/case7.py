n = int(input())
m = float(input())
if n == 1:
    print(m)
elif n == 2:
    print(m / 1000000)
elif n == 3:
    print(m / 1000)
elif n == 4:
    print(m * 1000)
else:
    print(m * 100)
