c = float(input())

left = 0
right = c ** 0.5

while right - left > 0.000001:
    x = (right + left) / 2

    if x ** 2 + (x + 1) ** 0.5 < c:
        left = x
    else:
        right = x

print(x)
