import sys


n = int(input())
segm = [[0, 0, 0, 0]]
for i in range(1, n + 1):
    t_1, t_2, a = map(int, sys.stdin.readline().split())
    diff = t_2 - t_1
    V_0 = segm[i - 1][2]
    V = V_0 + a * diff
    S = int(segm[i - 1][3] + V_0 * diff + 0.5 * a * diff ** 2)

    segm.append([t_2, a, V, S])

q = int(input())
for _ in range(q):
    d = int(sys.stdin.readline())

    left = 0
    right = n
    while right - left > 1:
        mid = (left + right) // 2
        if segm[mid][3] <= d:
            left = mid
        else:
            right = mid

    x_0 = segm[left][3]
    V_0 = segm[left][2]
    a = segm[left + 1][1]
    t_0 = segm[left][0]

    if a != 0:
        D = V_0 ** 2 + 2 * a * (d - x_0)
        t = int((-V_0 + D ** 0.5) / a)
    else:
        t = int((d - x_0) / V_0)

    print(t_0 + t)
