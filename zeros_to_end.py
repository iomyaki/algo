def pop_zeros(arr):
    last_not_nul = -1
    for i in range(len(arr)):
        if arr[i] != 0:
            last_not_nul += 1
            if i != last_not_nul:
                arr[last_not_nul], arr[i] = arr[i], arr[last_not_nul]
    return arr


def main():
    """
    Takes an array and moves zero values to its end
    """

    print(*pop_zeros([0, 1, 0, 3, 12]))
    print(*pop_zeros([9, 0, 1, 0, 3, 12]))
    print(*pop_zeros([0, 0, 0, 0, 3, 0, 2]))


if __name__ == "__main__":
    main()
