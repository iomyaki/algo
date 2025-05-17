import sys


def main():
    s = sys.stdin.readline().rstrip()
    if s[0] == s[2] or s[0] == s[3] or s[1] == s[3]:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
