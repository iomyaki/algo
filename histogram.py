#hist = [1, 3, 4, 2, 5, 4, 3, 1]
hist = [0, 2, 2, 2, 0]

n = len(hist)
stack = [(float('-inf'), -1)]
max_area = -1

for i in range(n):
    while stack[-1][0] >= hist[i]:
        max_area = max(max_area, stack.pop()[0] * (i - 1 - stack[-1][1]))
    stack.append((hist[i], i))

while stack[-1][0] >= 0:
    max_area = max(max_area, stack.pop()[0] * (n - 1 - stack[-1][1]))

print(max_area)
