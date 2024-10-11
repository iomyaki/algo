import sys
from heapq import heappush, heappop


def main():
    n, k = map(int, sys.stdin.readline().split())
    m = int(input())
    fence = []
    for i in range(m):
        c, l, r = map(int, sys.stdin.readline().split())
        fence.append((i, "+", l, c))
        fence.append((i, "-", r, c))
    fence.sort(key=lambda x: (x[2], -x[0]))
    #print(fence)

    h = []  # куча: (время, цвет)
    b = [False for _ in range(m)]  # на времена
    color_count = [None] + [0 for _ in range(k)]  # на цвета
    #print(color_count)

    if m > 0:
        prev = fence[0][2] - 1

    for i in range(len(fence)):
        #print(f"current entry: {fence[i]}")

        time, ty, coord, color = fence[i]

        if ty == "+":
            b[time] = True
            heappush(h, (-time, color))
        else:
            b[time] = False

        #print(f"h content: {h}")
        #print(f"booleans: {b}")

        color_count[h[0][1]] += coord - prev
        #print(f"added {coord - prev} to {h[0][1]}")
        prev = coord

        while h and not b[-h[0][0]]:
            heappop(h)

        if len(h) <= 0 and i + 1 < len(fence):
            prev = max(fence[i + 1][2] - 1, coord)

        #print(f"heap size on step {entry}: {len(h)}")
        #print("========================")

    print(*color_count[1:])


if __name__ == "__main__":
    main()

# WA test 8

"""
Привет, кажется проблема с границами
10 5 
5    
1 1 1
2 1 3
3 3 3
4 3 5
5 5 5

Выдает
0 1 0 2 2
Должен 
0 2 0 2 1

Если что-то советовать, то рекомендую точки типа 'r' складывать в вектор с координатой r + 1 и рассматривать исходные
данные не как отрезки, а как лучи: [l, r+1), тогда если возникнут коллизии на границах, то ты вначале удаляешь все точки
типа 'r', а только потом основная логика происходит
"""
