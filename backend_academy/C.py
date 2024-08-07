def lcg(e, a, m):
    return (a * e + 11) % m


def generator(seed, n, k, a, m):
    coins_given = 0
    sum_inserted = 0
    candies_got = 0
    req = 3 * k
    while True:
        seed = lcg(seed, a, m)
        coin = (abs(seed % 3 - 1) * 5 + abs(seed % 3) * 2) % 8
        coins_given += 1

        sum_inserted += coin
        if sum_inserted >= req:
            candies_got += sum_inserted // 3
            sum_inserted %= 3

        if candies_got >= n:
            return coins_given


def main():
    n, k, a, m = map(int, input().split())
    print(generator(0, n, k, a, m))


if __name__ == "__main__":
    main()
