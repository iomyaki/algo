expression = list(input().split())

answer = []
for i in expression:
    if i in '+-*':
        b = answer.pop()
        a = answer.pop()
        if i == '+':
            answer.append(a + b)
        elif i == '-':
            answer.append(a - b)
        elif i == '*':
            answer.append(a * b)
    else:
        answer.append(int(i))

print(answer[0])
