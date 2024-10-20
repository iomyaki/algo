_ = input()
numbers = tuple(set(map(int, input().split())))

processed = [numbers[0]]
in_a_row = False
for i in range(1, len(numbers)):
    if numbers[i] - numbers[i - 1] > 1:
        if in_a_row:
            in_a_row = False
            if numbers[i - 1] - processed[-1] > 1:
                processed.append('...')
            processed.append(numbers[i - 1])

        processed.append(numbers[i])
    else:
        in_a_row = True
else:
    if in_a_row:
        if numbers[-1] - processed[-1] > 1:
            processed.append('...')

        processed.append(numbers[-1])

print(*processed)
