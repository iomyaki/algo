import sys


def get_term(num: int) -> int:
    term = 1
    while num > 1:
        num //= 2
        term *= 2

    return term


def solution(num: int) -> int:
    if num < 7:
        return -1

    term_1 = get_term(num - 3)

    num -= term_1
    term_2 = get_term(num - 1)
    if term_2 >= term_1:
        term_2 = term_1 // 2

    num -= term_2
    term_3 = get_term(num)
    if term_3 >= term_2:
        term_3 = term_2 // 2

    return term_1 + term_2 + term_3


def main() -> None:
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        print(solution(int(sys.stdin.readline().rstrip())))


if __name__ == "__main__":
    main()
