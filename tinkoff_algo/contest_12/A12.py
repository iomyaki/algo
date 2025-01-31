def gcd(a: int, b: int) -> int:  # НОД
    while b > 0:
        a, b = b, a % b

    return a


def lcm(a: int, b: int) -> int:  # НОК
    return (a // gcd(a, b)) * b


def main() -> None:
    n, k = map(int, input().split())
    print(lcm(n, k))


if __name__ == '__main__':
    main()
