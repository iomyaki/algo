def power(n, p, mod):
    if p == 1:
        return n
    elif p % 2 == 0:
        return power(n, p // 2, mod) ** 2 % mod
    else:
        return power(n, p - 1, mod) * n % mod


def main():
    n, m, k, mod = map(int, input().split())

    combs = power(m, n, mod)
    denominator = power(k, mod - 2, mod)
    res = combs * denominator % mod

    print(res)


if __name__ == '__main__':
    main()
