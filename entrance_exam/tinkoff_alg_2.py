_ = input()
text = input()

ln = 0
min_len, max_len = float('inf'), float('-inf')

for symbol in text:
    if symbol != '#':
        ln += 1
    else:
        if ln < min_len:
            min_len = ln

        if ln > max_len:
            max_len = ln

        ln = 0
else:
    if ln < min_len:
        min_len = ln

    if ln > max_len:
        max_len = ln

print(min_len, max_len)
