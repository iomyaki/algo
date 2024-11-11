"""
A list of n integers is called a permutation if it contains all integers from 1 to n exactly once.
Inversion in the permutation is a pair of indices i, j that i < j and list[i] > list[j].
The task is: to create a permutation of the length n with k inversions.
1 <= n <= 3 * 10 ** 5
0 <= k <= n * (n - 1) / 2
"""

# n, k = tuple(map(int, input().split(' ')))
n, k = 5, 10  # for testing

if k == 0:
    print(*[i + 1 for i in range(n)])
elif k <= n - 1:
    part_1 = [i for i in range(1, k + 1)]
    part_2 = [0]
    part_3 = [j for j in range(k + 1, n)]
    result = part_1 + part_2 + part_3
    print(*[i + 1 for i in result])
else:
    sub = 1
    while k > n - 1:
        k -= (n - sub)
        sub += 1
    k -= (n - sub)

    part_1 = [i for i in range(sub + 1, k + sub + 1)]
    part_2 = [sub] if n - k != 0 else []
    part_3 = [j for j in range(k + sub + 1, n)]
    part_4 = [k for k in range(sub - 1, -1, -1)]
    result = part_1 + part_2 + part_3 + part_4
    print(*[i + 1 for i in result])
