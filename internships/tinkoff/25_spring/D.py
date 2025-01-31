import sys


def gcd(a: int, b: int) -> int:
    while b > 0:
        a, b = b, a % b

    return a


def lcm(a: int, b: int) -> int:
    return (a // gcd(a, b)) * b


def to_add(num: int, mod: int) -> int:
    return (mod - (num % mod)) % mod


def main() -> None:
    n, x, y, z = map(int, sys.stdin.readline().split())
    arr = tuple(map(int, sys.stdin.readline().split()))

    lcm_xy = lcm(x, y)
    lcm_xz = lcm(x, z)
    lcm_yz = lcm(y, z)
    lcm_xyz = lcm(lcm_xy, z)

    dp = [[float("inf") for _ in range(8)] for _ in range(n)]
    for i in range(n):
        num = arr[i]
        dp[i][1] = to_add(num, x)
        dp[i][2] = to_add(num, y)
        dp[i][4] = to_add(num, z)
        dp[i][3] = to_add(num, lcm_xy)
        dp[i][5] = to_add(num, lcm_xz)
        dp[i][6] = to_add(num, lcm_yz)
        dp[i][7] = to_add(num, lcm_xyz)

    for i in range(1, n):
        new = [float("inf") for _ in range(8)]
        for m1 in range(1, 8):
            new[m1] = min(dp[i][m1], dp[i - 1][m1])
        for m2 in range(1, 8):
            for m3 in range(1, 8):
                m4 = m2 | m3
                new[m4] = min(new[m4], dp[i][m3] + dp[i - 1][m2])
        dp[i] = new

    print(dp[n - 1][7])


if __name__ == "__main__":
    main()
