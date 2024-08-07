from itertools import permutations


perms = permutations([i for i in range(1, 10)])

counter = 0
for perm in perms:
    a, b, c, d, e, f, g, h, i = perm
    if a > b > c and d > e > f and i < h < g < d < a and b > e > h and c > f > i:
        print(perm)
        counter += 1

print(counter)
