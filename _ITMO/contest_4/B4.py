import sys


def insertion_sort(arr):
    comparisons = 0
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            comparisons += 1

        arr[j + 1] = key

        if j >= 0:
            comparisons += 1

    return comparisons


def main():
    sys.stdin.readline()
    array = list(map(int, sys.stdin.readline().split()))
    print(insertion_sort(array))


if __name__ == "__main__":
    main()
