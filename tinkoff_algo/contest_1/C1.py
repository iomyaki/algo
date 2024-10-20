import sys


def query(x):
    print(x)
    sys.stdout.flush()
    return input()


n = int(input())

if n == 1:
    print('! 1')
else:
    left = 1
    right = n
    counter = 0
    while left != right - 1:
        mid = (left + right) // 2

        counter += 1
        if query(mid) == '<':
            right = mid
        else:
            left = mid

        if counter == 25:
            break

    if counter < 25:
        if query(right) == '<':
            print(f'! {left}')
        else:
            print(f'! {right}')
