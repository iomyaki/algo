def qsort(a, left, right):
    global comparisons

    if right <= left:
        return
    q = a[(left + right) // 2]
    i = left
    j = right
    while i <= j:
        while a[i] < q:
            i += 1
            comparisons += 1
        comparisons += 1
        while q < a[j]:
            j -= 1
            comparisons += 1
        comparisons += 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    qsort(a, left, j)
    qsort(a, i, right)


comparisons = 0

lst = [2, 4, 6, 8, 1, 3, 5, 7]

qsort(lst, 0, len(lst) - 1)

print(comparisons)
