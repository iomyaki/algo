def Euclid(a, b):
    while b > 0:
        a %= b
        a, b = b, a

    return a


def main():
    n, k = map(int, input().split())
    gcd = Euclid(n, k)
    lcm = n * k // gcd
    print(lcm)


if __name__ == '__main__':
    main()
