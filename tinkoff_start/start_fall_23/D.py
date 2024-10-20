from itertools import combinations_with_replacement


n, m = tuple(map(int, input().split(' ')))
denoms = list(map(int, input().split(' ')))

found = False

for i in range(1, m * 2 + 1):
    for comb in combinations_with_replacement(denoms * 2, i):
        if sum(comb) == n:
            found = True
            print(len(comb))
            print(*comb)
            break
    if found:
        break

if not found:
    print('-1')
