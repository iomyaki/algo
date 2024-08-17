n, m = tuple(map(int, input().split(' ')))

ghosts = {i: [{i}] for i in range(1, n + 1)}

answer = ''

for j in range(m):
    question = tuple(map(int, input().split(' ')))
    if question[0] == 1:
        for ghost in ghosts[question[1]][-1]:
            ghosts[ghost].append(ghosts[ghost][-1] | ghosts[question[2]][-1])
        for ghost in ghosts[question[2]][-1]:
            ghosts[ghost].append(ghosts[ghost][-1] | ghosts[question[1]][-1])
    elif question[0] == 2:
        if question[2] in ghosts[question[1]][-1]:
            answer += 'YES\n'
        else:
            answer += 'NO\n'
    else:
        answer += str(len(ghosts[question[1]])) + '\n'

print(answer.rstrip())
