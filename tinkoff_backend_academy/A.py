def main():
    _ = input()
    socks = list(map(int, input().split()))

    even = True
    for sock in socks:
        if even and sock % 2 == 1:
            even = False
        elif not even and sock % 2 == 1:
            even = True

    if even:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
