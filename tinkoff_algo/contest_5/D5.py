s = input()

if set(s) == 1:
    print(s)
else:
    ss = s * 2

    len_s = len(s)
    min_str = s

    for i in range(len_s):
        shift = ss[i:i + len_s]
        if shift < min_str:
            min_str = shift

    print(min_str)
