n = int(input())
lst = tuple(map(int, input().split()))

prefix_sum, prefix_xor = [0], [0]

for i in range(n):
    prefix_sum.append(prefix_sum[i] + lst[i])
    prefix_xor.append(prefix_xor[i] ^ lst[i])

for _ in range(int(input())):
    t, l, r = input().split()
    if t == '1':
        print(prefix_sum[int(r)] - prefix_sum[int(l) - 1])
    else:
        print(prefix_xor[int(r)] ^ prefix_xor[int(l) - 1])
