import sys


def mod_exp(base: int, exp: int, mod: int) -> int:
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result


def main() -> None:
    n = int(sys.stdin.readline())

    mod = 10 ** 9 + 7
    summ = 0
    sign = -1 if n % 2 == 0 else 1
    bino = 1
    pow_2 = 1
    for k in range(n):
        term = (sign * bino * pow_2) % mod
        summ = (summ + term) % mod
        sign = -sign

        if k < n - 1:
            bino = (bino * (n - 1 - k) * pow(mod_exp(k + 1, mod - 2, mod), 1, mod)) % mod
        pow_2 = (pow_2 * mod_exp(2, k, mod)) % mod

    result = (summ * n) % mod
    print(result)


if __name__ == "__main__":
    main()
