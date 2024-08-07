n = int(input())
hist = list(map(int, input().split()))

stack = [(float('-inf'), -1)]
area = -1

for i in range(n):
    if stack[-1][0] < hist[i]:
        stack.append((hist[i], i))
    else:
        while stack[-1][0] >= hist[i]:
            area = max(area, stack.pop()[0] * (i - 1 - stack[-1][1]))
        stack.append((hist[i], i))

while stack[-1][0] >= 0:
    area = max(area, stack.pop()[0] * (n - 1 - stack[-1][1]))

print(area)
