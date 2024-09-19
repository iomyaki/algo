def main():
    l, r = map(int, input().split())

    for i in range(l, r + 1):
        i_str = str(i)
        if len(i_str) == len(set(i_str)):
            print(i)
            break
    else:
        print(-1)


if __name__ == "__main__":
    main()
