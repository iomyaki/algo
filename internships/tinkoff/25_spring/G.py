import sys

MOD = 998244353


def main() -> None:
    n, k = map(int, sys.stdin.readline().split())
    numbers = tuple(map(int, sys.stdin.readline().split()))

    numb_pow = [1 for _ in range(n)]
    sum_p = [0 for _ in range(301)]
    sum_p[0] = n

    for power in range(1, 301):
        current_sum = 0
        for i in range(n):
            numb_pow[i] = numb_pow[i] * numbers[i] % MOD
            current_sum = (current_sum + numb_pow[i]) % MOD
        sum_p[power] = current_sum

    del numbers
    del numb_pow

    binom = [[0 for _ in range(301)] for _ in range(301)]
    binom[0][0] = 1
    for power in range(1, 301):
        binom[power][0] = 1
        binom[power][power] = 1
        for i in range(1, power):
            binom[power][i] = (binom[power - 1][i] + binom[power - 1][i - 1]) % MOD

    denominator = (MOD + 1) >> 1
    for power in range(1, k + 1):
        result = 0
        for i in range(power + 1):
            factor = ((sum_p[i] * sum_p[power - i] % MOD - sum_p[power] + MOD) % MOD) * binom[power][i] % MOD
            factor = factor * denominator % MOD
            result = (result + factor) % MOD

        print(result)


if __name__ == "__main__":
    main()
