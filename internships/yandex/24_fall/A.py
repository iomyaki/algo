import sys


def main() -> None:
    r, _ = map(int, sys.stdin.readline().split())
    cross_r = []
    for _ in range(r):
        cross_r.append(sys.stdin.readline().rstrip())

    cross_c_pre = tuple(zip(*cross_r))
    cross_c = []
    for tup in cross_c_pre:
        str_sum = ""
        for c in tup:
            str_sum += c
        cross_c.append(str_sum)

    all_words = []
    for row in cross_r:
        words = row.split("#")
        for word in words:
            if len(word) >= 2:
                all_words.append(word)

    for col in cross_c:
        words = col.split("#")
        for word in words:
            if len(word) >= 2:
                all_words.append(word)

    all_words.sort()
    print(all_words[0])


if __name__ == "__main__":
    main()
