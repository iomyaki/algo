x_1, y_1 = map(float, input().split())
x_2, y_2 = map(float, input().split())
x_3, y_3 = map(float, input().split())

rs = ((x_1 ** 2 + y_1 ** 2) ** 0.5, (x_2 ** 2 + y_2 ** 2) ** 0.5, (x_3 ** 2 + y_3 ** 2) ** 0.5)

score = 0
for r in rs:
    if r <= 0.1:
        score += 3
    elif r <= 0.8:
        score += 2
    elif r <= 1:
        score += 1

print(score)
