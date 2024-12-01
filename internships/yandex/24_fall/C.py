import sys
from collections import Counter


def main() -> None:
    n = int(sys.stdin.readline())
    row_1 = tuple(map(int, sys.stdin.readline().split()))
    row_2 = tuple(map(int, sys.stdin.readline().split()))
    row_3 = tuple(map(int, sys.stdin.readline().split()))

    cnt = 0
    col = [True for _ in range(n)]
    dict_row_1 = Counter(row_1)
    dict_row_2 = Counter(row_2)
    dict_row_3 = Counter(row_3)
    set_row_1 = set()
    set_row_2 = set(row_1) - set(row_2)
    set_row_3 = set(row_1) - set(row_3)
    set_united = set_row_1 | set_row_2 | set_row_3

    while not set_row_1 == set_row_2 == set_row_3:
        for i in range(n):
            if col[i] and (row_1[i] in set_united or row_2[i] in set_united or row_3[i] in set_united):
                col[i] = False
                cnt += 1

                dict_row_1[row_1[i]] -= 1
                if dict_row_1[row_1[i]] == 0:
                    set_row_1.add(row_1[i])
                    set_united.add(row_1[i])

                dict_row_2[row_2[i]] -= 1
                if dict_row_2[row_2[i]] == 0:
                    set_row_2.add(row_2[i])
                    set_united.add(row_2[i])

                dict_row_3[row_3[i]] -= 1
                if dict_row_3[row_3[i]] == 0:
                    set_row_3.add(row_3[i])
                    set_united.add(row_3[i])

    print(cnt)


if __name__ == "__main__":
    main()
