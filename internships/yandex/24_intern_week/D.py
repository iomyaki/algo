import sys
from math import ceil, sqrt


def gcd(a: int, b: int) -> int:
    while b > 0:
        a %= b
        a, b = b, a

    return a


def max_in_prime_fact(n: int) -> int:
    max_p = -1
    for i in range(2, ceil(sqrt(n)) + 1):
        while n % i == 0:
            n //= i
            max_p = max(max_p, i)

    max_p = max(max_p, n)
    return max_p


def main() -> None:
    t = int(sys.stdin.readline())
    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        gcd_a_b = gcd(a, b)
        a_red, b_red = a // gcd_a_b, b // gcd_a_b
        print(gcd_a_b * max(max_in_prime_fact(a_red), max_in_prime_fact(b_red)))


if __name__ == "__main__":
    main()
