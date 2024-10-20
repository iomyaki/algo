def bin_search(array):
    l, r = -1, len(array)
    while r - l > 1:
        m = (l + r) // 2
        if array[m] == 0:
            l = m
        else:
            r = m

    return l, r


def main():
    input()
    print(*bin_search(tuple(map(int, " ".join(list(input())).split()))))


if __name__ == "__main__":
    main()
