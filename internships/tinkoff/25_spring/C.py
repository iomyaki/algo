import sys


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    days = tuple(map(int, sys.stdin.readline().split()))

    first, second = days[0], days[1]
    the_rest = list(days[2:])
    del days

    the_rest.sort()
    result = float("inf")
    for r in range(m - 1, n - 2):
        l = r - m + 1
        d_first, d_second = 0, 0
        if first > the_rest[l]:
            d_first = first - the_rest[l]
        if second < the_rest[r]:
            d_second = the_rest[r] - second
        result = min(result, d_first + d_second)

    print(result)


if __name__ == "__main__":
    main()
