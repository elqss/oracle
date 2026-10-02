N = int(input())

found = False

while N > 0:
    if N % 2 == 1:
        found = True
    N //= 10

if found:
    print("TRUE")
else:
    print("FALSE")
