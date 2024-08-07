# https://youtu.be/RZtM3GIeS-4?t=2910

s = input()
n = len(s)
d = []
pos = []

for i in range(n):
    d.append([0 for _ in range(n)])
    pos.append([0 for _ in range(n)])

for i in range(n):
    for j in range(n):
        if i == j:
            d[i][j] = 1

#print(d)

for right in range(n):
    for left in range(right, -1, -1):
        if left == right:
            d[left][right] = 1
        else:
            min = float('inf')
            mink = -1
            b1 = s[left] == '(' and s[right] == ')'
            b2 = s[left] == '[' and s[right] == ']'
            b3 = s[left] == '{' and s[right] == '}'
            if b1 or b2 or b3:
                min = d[left + 1][right - 1]
            for k in range(left, right):
                if min > d[left][k] + d[k + 1][right]:
                    min = d[left][k] + d[k + 1][right]
                    mink = k
            d[left][right] = min
            pos[left][right] = mink


def rec(l, r):
    temp = r - l + 1
    if d[l][r] == temp:
        return
    if d[l][r] == 0:
        print(s[l:r + 1], end="")
        return
    if pos[l][r] == -1:
        print(s[l], end="")
        rec(l + 1, r - 1)
        print(s[r], end="")
        return
    rec(l, pos[l][r])
    rec(pos[l][r] + 1, r)


rec(0, n - 1)
