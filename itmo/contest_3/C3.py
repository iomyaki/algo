def lower_bound(array, target):
    l, r = -1, len(array)
    while r - l > 1:
        m = (l + r) // 2
        if array[m] < target:
            l = m
        else:
            r = m

    return r


def upper_bound(array, target):
    l, r = -1, len(array)
    while r - l > 1:
        m = (l + r) // 2
        if array[m] <= target:
            l = m
        else:
            r = m

    return r


def main():
    input()
    array = sorted(list(map(int, input().split())))
    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split())
        print(upper_bound(array, b) - lower_bound(array, a))


if __name__ == "__main__":
    main()
