n, m, k = map(int, input().split())

points = {i + 1: {} for i in range(n)}

for _ in range(m):
    car_data = tuple(map(int, input().split()))
    points[car_data[0]][car_data[1]] = car_data[2]

route = tuple(map(int, input().split()))

point = 1
try:
    for car in route:
        point = points[point][car]
    print(point)

except KeyError:
    print(0)
