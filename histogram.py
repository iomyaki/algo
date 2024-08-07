hist = [1, 3, 4, 2, 5, 4, 3, 1]

hist_len = len(hist)
stack = [(float('-inf'), -1)]
area = -1

for i in range(hist_len):
    if stack[-1][0] < hist[i]:
        stack.append((hist[i], i))
    else:
        while stack[-1][0] >= hist[i]:
            area = max(area, stack.pop()[0] * (i - 1 - stack[-1][1]))
        stack.append((hist[i], i))

while stack[-1][0] >= 0:
    area = max(area, stack.pop()[0] * (hist_len - 1 - stack[-1][1]))

print(area)
