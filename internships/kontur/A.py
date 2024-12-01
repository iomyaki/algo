import sys


def main() -> None:
    n = int(sys.stdin.readline())
    symbols, most_impressive = 0, ""
    for _ in range(n):
        str_curr = sys.stdin.readline().rstrip()
        symbols_curr = len(set(str_curr))
        if symbols_curr > symbols:
            symbols = symbols_curr
            most_impressive = str_curr

    print(f"{symbols} {most_impressive}")


if __name__ == "__main__":
    main()
