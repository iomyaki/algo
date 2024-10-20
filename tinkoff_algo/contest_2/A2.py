n = int(input())

stack = []

for _ in range(n):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        if len(stack) == 0:
            stack.append((query[1], query[1]))
        else:
            stack.append((query[1], min(query[1], stack[-1][1])))
    elif query[0] == 2:
        stack.pop()
    else:
        print(stack[-1][1])
