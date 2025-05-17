import sys


def main():
    n, a, b = map(int, sys.stdin.readline().split())
    seq = sys.stdin.readline().rstrip()

    balance, min_balance, opening = 0, 0, 0
    for parenthesis in seq:
        if parenthesis == '(':
            balance += 1
            opening += 1
        else:
            balance -= 1

        min_balance = min(min_balance, balance)

    negations = abs(n - opening)
    if opening < n:
        swaps = max(0, -min_balance - 2 * negations)
    else:
        swaps = -min_balance
    cost = ((swaps + 1) // 2) * min(a, 2 * b) + negations * b

    print(cost)


if __name__ == '__main__':
    main()
