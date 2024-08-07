n = int(input())
levels = tuple(map(int, input().split()))

if n > 1:
    road_means = 0
    for i in range(1, n):
        road_means += (levels[i - 1] + levels[i]) / 2

    print(road_means / (n - 1))
else:
    print(float(levels[0]))
