import sys


def main() -> None:
    n = int(sys.stdin.readline())
    row_1 = tuple(map(int, sys.stdin.readline().split()))
    row_2 = tuple(map(int, sys.stdin.readline().split()))
    row_3 = tuple(map(int, sys.stdin.readline().split()))

    cnt_row_1 = {i + 1: 1 for i in range(n)}
    cnt_row_2 = {i + 1: 0 for i in range(n)}
    cnt_row_3 = {i + 1: 0 for i in range(n)}
    idx_row_1 = {i + 1: [] for i in range(n)}
    idx_row_2 = {i + 1: [] for i in range(n)}
    idx_row_3 = {i + 1: [] for i in range(n)}
    set_row_1 = set()
    set_row_2 = set(row_1) - set(row_2)
    set_row_3 = set(row_1) - set(row_3)
    set_current = set_row_1 | set_row_2 | set_row_3
    excluded = set()
    exclude_now = set()

    for i in range(n):
        cnt_row_2[row_2[i]] += 1
        cnt_row_3[row_3[i]] += 1

        idx_row_1[row_1[i]].append(i)
        idx_row_2[row_2[i]].append(i)
        idx_row_3[row_3[i]].append(i)

    while not set_row_1 == set_row_2 == set_row_3:
        for m in set_current:
            for i in idx_row_1[m]:
                if i not in excluded:
                    exclude_now.add(i)
            for j in idx_row_2[m]:
                if j not in excluded:
                    exclude_now.add(j)
            for k in idx_row_3[m]:
                if k not in excluded:
                    exclude_now.add(k)
        set_current.clear()

        for idx in exclude_now:
            excluded.add(idx)

            cnt_row_1[row_1[idx]] -= 1
            if cnt_row_1[row_1[idx]] == 0:
                set_row_1.add(row_1[idx])
                set_current.add(row_1[idx])

            cnt_row_2[row_2[idx]] -= 1
            if cnt_row_2[row_2[idx]] == 0:
                set_row_2.add(row_2[idx])
                set_current.add(row_2[idx])

            cnt_row_3[row_3[idx]] -= 1
            if cnt_row_3[row_3[idx]] == 0:
                set_row_3.add(row_3[idx])
                set_current.add(row_3[idx])
        exclude_now.clear()

    print(len(excluded))


if __name__ == "__main__":
    main()
