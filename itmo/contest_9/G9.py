import sys


def main() -> None:
    k, _ = map(int, sys.stdin.readline().split())
    dct = {}
    for _ in range(k):
        value, key = sys.stdin.readline().rstrip().split(": ")
        dct[key] = value
    code = sys.stdin.readline()

    result = ""
    curr = ""
    for char in code:
        curr += char
        if curr in dct:
            result += dct[curr]
            curr = ""

    print(result)


if __name__ == "__main__":
    main()
