import sys
from copy import deepcopy


def main():
    q = int(input())
    for _ in range(q):
        _ = int(sys.stdin.readline())
        numbers = list(map(int, sys.stdin.readline().split()))
        numbers_dict = {}
        for num in numbers:
            numbers_dict[num] = numbers_dict.get(num, 0) + 1

        i = 1
        powers = [1]
        while i < 4096:
            i *= 2
            powers.append(i)

        while numbers_dict.get(2048, 0) < 1:
            dict_prev = deepcopy(numbers_dict)
            for pow in powers:
                if numbers_dict.get(pow, 0) > 1:
                    value = numbers_dict[pow] // 2
                    numbers_dict[pow] -= value * 2
                    numbers_dict[pow * 2] = numbers_dict.get(pow * 2, 0) + value

                    if numbers_dict.get(2048, 0) > 0:
                        break

            if dict_prev == numbers_dict:
                break

        if numbers_dict.get(2048, 0) > 0:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
