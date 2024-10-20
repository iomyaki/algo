n = int(input())

stack = []

for i in tuple(map(int, input().split())):
    if len(stack) == 0:
        stack.append((i, 1))
    else:
        if stack[-1][0] == i:
            stack.append((i, stack[-1][1] + 1))
        else:
            if stack[-1][1] >= 3:
                for _ in range(stack[-1][1]):
                    stack.pop()
                if stack[-1][0] == i:
                    stack.append((i, stack[-1][1] + 1))
                else:
                    stack.append((i, 1))
            else:
                stack.append((i, 1))

if stack[-1][1] >= 3:
    for _ in range(stack[-1][1]):
        stack.pop()

print(n - len(stack))
