"""
There are three players. The round is: score of the first player is now sum of scores of the second and the third,
then the score of the second is existing of first plus third, then third = first + second, e.g.:
(initial scores)
a, b, c = 1, 1, 1
(first round starts)
a, b, c = 2, 1, 1
a, b, c = 2, 3, 1
a, b, c = 2, 3, 5
Initial scores and number of rounds can be enormous, so you have to calculate them modulo 1,000,000,007
"""


def matrix_multiply(a, b, mod):
    return [
        [(a[0][0] * b[0][0] + a[0][1] * b[1][0]) % mod, (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % mod],
        [(a[1][0] * b[0][0] + a[1][1] * b[1][0]) % mod, (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % mod]
    ]


def matrix_power(matrix, n, mod):
    result = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, matrix, mod)
        matrix = matrix_multiply(matrix, matrix, mod)
        n //= 2
    return result


def fib(n, mod):
    if n == 0:
        return 0
    matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(matrix, n - 1, mod)
    return result_matrix[0][0]


n_plays = int(input())
for _ in range(n_plays):
    _, n = map(int, input().split())
    frens = tuple(map(int, input().split()))

    module = 10 ** 9 + 7

    a = (fib((n * 3 - 1) - 1, module) * frens[1] + fib((n * 3) - 1, module) * frens[2]) % module
    b = (fib((n * 3) - 1, module) * frens[1] + fib((n * 3 + 1) - 1, module) * frens[2]) % module
    c = (fib((n * 3 + 1) - 1, module) * frens[1] + fib((n * 3 + 2) - 1, module) * frens[2]) % module

    print(a, b, c)
