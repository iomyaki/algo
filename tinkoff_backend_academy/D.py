from itertools import product


def passable(var):
    up = var[0][0]
    dw = var[0][1]
    for i in range(1, len(var)):
        if up <= var[i][0] <= dw or up <= var[i][1] <= dw:
            up, dw = var[i][0], var[i][1]
        else:
            return False

    return True


def main():
    n, m = map(int, input().split())
    depot = []
    lengths = []
    for _ in range(m):
        s, t = map(int, input().split())
        depot.append((s, t))
        lengths.append(t - s + 1)

    way_variants = []
    for i in range(m):
        way = []
        for j in range(n - lengths[i] + 1):
            way.append((j + 1, j + lengths[i]))
        way_variants.append(way)

    variants = tuple(product(*way_variants))

    good_vars = []
    for var in variants:
        if passable(var):
            good_vars.append(var)

    min_moves = float("inf")
    for good in good_vars:
        counter = 0
        for i in range(m):
            counter += abs(good[i][0] - depot[i][0])
        min_moves = min(counter, min_moves)

    print(min_moves)


if __name__ == "__main__":
    main()
