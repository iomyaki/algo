lst = [5, 4, 1, 7, 7, 4, 3, 6, 1, 1, 1, 6, 1, 1, 1, 6, 5, 9, 9, 9, 1, 7, 1, 1, 1, 1]
orig_lst = []

length = len(lst)

i = 0
while i < length - 1:
    if lst[i] != lst[i + 1]:
        orig_lst.append(lst[i])
        i += 1
    else:
        i += 2

    if i == length - 1:
        orig_lst.append(lst[i])

print(orig_lst)
