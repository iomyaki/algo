def merge(ls1, ls2):
    global inv

    ls = []
    i, j = 0, 0
    length = len(ls1)

    while i < len(ls1) and j < len(ls2):
        if ls1[i] <= ls2[j]:
            ls.append(ls1[i])
            i += 1
        else:
            ls.append(ls2[j])
            inv += length - i
            j += 1

    if i < len(ls1):
        ls += ls1[i:]

    if j < len(ls2):
        ls += ls2[j:]

    return ls


inv = 0

#array = [1, 2, 3, 44, 45, 46, 4, 5, 6, 30, 31, 32, 7, 8, 9]
#array = [1, 3, 6, 11, 15, 16, 17, 82, 91, 100, 102, -1, 0, 2, 3, 4, 5, 13, 14]

_ = input()
array = tuple(map(int, input().split()))

fragmented = [[i] for i in array]

counter = 0
while len(fragmented) != 1:
    new = []
    for i in range(1, len(array), 2):
        try:
            new.append(merge(fragmented[i - 1], fragmented[i]))
        except IndexError:
            pass

    if len(fragmented) % 2 != 0:
        new.append(fragmented[-1])

    fragmented = new

print(inv)
print(*fragmented[0])
