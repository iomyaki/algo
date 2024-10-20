def power(n, p, mod):
    if p == 1:
        return n
    elif p % 2 == 0:
        return power(n, p // 2, mod) ** 2 % mod
    else:
        return power(n, p - 1, mod) * n % mod


def main():
    n, k = map(int, input().split())
    mod = 10 ** 9 + 7

    numerator = 1
    for i in range(n - k + 1, n + 1):
        numerator = numerator * i % mod

    k_fact = 1
    for i in range(2, k + 1):
        k_fact = k_fact * i % mod

    denominator = power(k_fact, mod - 2, mod)
    bin_coeff = numerator * denominator % mod

    print(bin_coeff)


if __name__ == '__main__':
    main()
