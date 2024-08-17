def rotate_matrix_operations(n, direction):
    swaps = []
    layers = n // 2

    for layer in range(layers):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = (first, i)
            right = (i, last)
            bottom = (last, last - offset)
            left = (last - offset, first)

            if direction == 'R':
                swaps.append((top, left))
                swaps.append((left, bottom))
                swaps.append((bottom, right))
            elif direction == 'L':
                swaps.append((top, right))
                swaps.append((right, bottom))
                swaps.append((bottom, left))

    print(len(swaps))
    for swap in swaps:
        x1, y1 = swap[0]
        x2, y2 = swap[1]
        print(f'{x1} {y1} {x2} {y2}')


n, direction = input().split()
n = int(n)
for _ in range(n):
    _ = input()

rotate_matrix_operations(n, direction)
