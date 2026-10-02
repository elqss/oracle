A = int(input())
B = int(input())

while B != 0:
    A, B = B, A % B

print(A)
