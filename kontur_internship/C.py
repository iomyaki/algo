import sys


def main() -> None:
    n, k, q = map(int, sys.stdin.readline().split())
    buildings = tuple(map(int, sys.stdin.readline().split()))

    left, right = 0, 0
    while right < n:
        if buildings[right] >= k:
            q -= 1
        if q < 0:
            if buildings[left] >= k:
                q += 1
            left += 1
        right += 1

    print(right - left)


if __name__ == "__main__":
    main()
