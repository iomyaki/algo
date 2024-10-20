def last_fact_digit(n):
    j = 1
    d_2, d_5 = 0, 0
    for k in range(2, n + 1):
        i = k
        while i % 2 == 0:
            i //= 2
            d_2 += 1
        while i % 5 == 0:
            i //= 5
            d_5 += 1

        j = j * i % 10

    for _ in range(d_2 - d_5):
        j = j * 2 % 10

    return j


def main():
    print(last_fact_digit(int(input())))


if __name__ == '__main__':
    main()
