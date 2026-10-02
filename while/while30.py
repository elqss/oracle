A = float(input())
B = float(input())
C = float(input())

count = 0
x = 0.0

while x + C <= A:
    x += C
    count += 1

y = 0.0

while y + C <= B:
    y += C

print(count * (int(y / C)))
