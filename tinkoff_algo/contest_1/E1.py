a, b, c, d = map(int, input().split())

left = -10000
right = 10000

while right - left > 0.00001:
    x = (right + left) / 2

    if a * x ** 3 + b * x ** 2 + c * x + d < 0:
        if a > 0:
            left = x
        else:
            right = x
    elif a * x ** 3 + b * x ** 2 + c * x + d > 0:
        if a > 0:
            right = x
        else:
            left = x
    else:
        print(x)
        break
else:
    print(x)
