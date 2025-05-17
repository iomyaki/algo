import sys


def main():
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().split()))

    arr.sort(reverse=True)
    encountered = set()
    for i in range(n):
        number = arr[i]
        while number >= 0:
            if number not in encountered:
                encountered.add(number)
                break
            if number == 0:
                break

            number //= 2

    print(len(encountered))


if __name__ == '__main__':
    main()
