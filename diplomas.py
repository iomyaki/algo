def check(side, w, h, n):
    return (side // w) * (side // h) >= n


def main():
    w, h, n = map(int, input().split())

    left = 0
    right = 10 ** 18
    while right - left > 1:
        mid = left + (right - left) // 2
        if check(mid, w, h, n):
            right = mid
        else:
            left = mid

    print(right)


if __name__ == '__main__':
    main()
