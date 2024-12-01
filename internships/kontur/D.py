import sys


def upper_bound(array: tuple, target: int) -> int:
    l, r = -1, len(array)
    while r - l > 1:
        m = (l + r) // 2
        if array[m] <= target:
            l = m
        else:
            r = m

    return r


def main() -> None:
    _, _ = map(int, sys.stdin.readline().split())
    u, v = map(int, sys.stdin.readline().split())
    vert = tuple(sorted(map(int, sys.stdin.readline().split())))
    hor = tuple(sorted(map(int, sys.stdin.readline().split())))

    for _ in range(int(sys.stdin.readline())):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

        if x2 < x1:
            x1, x2 = x2, x1
        if y2 < y1:
            y1, y2 = y2, y1

        same = True

        v_idx = upper_bound(vert, x1)
        if v_idx < u and vert[v_idx] < x2:
            same = False

        h_idx = upper_bound(hor, y1)
        if h_idx < v and hor[h_idx] < y2:
            same = False

        if same:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
