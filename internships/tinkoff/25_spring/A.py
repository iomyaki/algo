import sys


def main() -> None:
    s = sys.stdin.readline().rstrip()
    print("Yes" if s.find("R") < s.find("M") else "No")


if __name__ == "__main__":
    main()
