import sys


def main():
    sys.stdin.readline()
    numbers = tuple(map(int, sys.stdin.readline().split()))
    ctn = [0 for _ in range(101)]
    for num in numbers:
        pos = 0
        i = 1
        while i <= num:
            pos += ctn[i]
            i += 1
        ctn[num] += 1
        print(pos, end=" ")


if __name__ == "__main__":
    main()
