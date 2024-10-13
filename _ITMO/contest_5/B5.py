import sys


def qsort(left, right, depth):
    global array, depth_global

    depth_global = max(depth_global, depth)
    if right <= left:
        return

    # partition
    x = array[(left + right) // 2]
    A, B, C = [], [], []
    for i in range(left, right + 1):
        if array[i] < x:
            A.append(array[i])
        elif array[i] == x:
            B.append(array[i])
        else:
            C.append(array[i])

    array[left:right + 1] = A + B + C
    qsort(left, left + len(A) - 1, depth + 1)
    qsort(left + len(A) + len(B), right, depth + 1)


sys.stdin.readline()
array = list(map(int, sys.stdin.readline().split()))
depth_global = 0
qsort(0, len(array) - 1, 0)
print(depth_global)
