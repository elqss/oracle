P = float(input())

day = 1
run = 10.0
S = 10.0

while S <= 200:
    run += run * P / 100
    S += run
    day += 1

print(day, S)
