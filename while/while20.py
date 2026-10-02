N = int(input())

found = False

while N > 0:
    if N % 10 == 2:
        found = True
    N //= 10

if found:
    print("TRUE")
else:
    print("FALSE")
