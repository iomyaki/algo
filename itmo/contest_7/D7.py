def main() -> None:
    numbers = []
    max_num = -1
    while True:
        try:
            n = int(input())
            numbers.append(n)
            max_num = max(max_num, n)
        except EOFError:
            break

    limit = max_num + 1
    dp = [limit for _ in range(limit)]
    dp[0], dp[1] = 0, 1
    n, n_cubed = 1, 1
    for i in range(2, limit):
        while n_cubed <= i:
            if i == n_cubed:
                dp[i] = 1
            elif dp[i] > dp[i - n_cubed]:
                dp[i] = dp[i - n_cubed] + 1
            n += 1
            n_cubed = n ** 3
        n, n_cubed = 1, 1

    for number in numbers:
        print(dp[number])


if __name__ == "__main__":
    main()
