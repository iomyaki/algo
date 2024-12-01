import sys


def main() -> None:
    n = int(sys.stdin.readline())

    terms = []
    now = 1
    while n > 0:
        if n - now >= now + 1:
            terms.append(now)
            n -= now
            now += 1
        else:
            terms.append(n)
            break

    print(len(terms))
    print(*terms)


if __name__ == "__main__":
    main()
