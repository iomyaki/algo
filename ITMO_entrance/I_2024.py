x, y = map(float, input().split())

s = x
days = 1
while s < y - 1e-7:
    x *= 1.7
    s += x
    days += 1

print(days)
