def bin_search(array, target):
    l, r = -1, len(array)
    while r - l > 1:
        m = (l + r) // 2
        if array[m] <= target:
            l = m
        else:
            r = m

    return array[l] == target


def main():
    input()
    seq = tuple(map(int, input().split()))
    queries = tuple(map(int, input().split()))
    for q in queries:
        if bin_search(seq, q):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
