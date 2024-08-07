def merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2

        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


def merge(arr, l, m, r):
    n1, n2 = m - l + 1, r - m
    arr1, arr2 = arr[l:m + 1], arr[m + 1:r + 1]

    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = arr1[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = arr2[j]
        j += 1
        k += 1


arr = [1, 3, 6, 11, 15, 16, 17, 82, 91, 100, 102, -1, 0, 2, 3, 4, 5, 13, 14]
merge_sort(arr, 0, len(arr) - 1)
print(*arr)
