from math import ceil


n, m = map(int, input().split())
comps = []
for_answer = []
for number in range(m):
    t, b, y = map(int, input().split())
    for_answer.append((t, b, y))
    if n % b != 0:
        comps.append([number, 1 / ((n // b) * (t * b + y) + n % b)])
    else:
        comps.append([number, 1 / ((n // b) * (t * b + y) - y)])

comps.sort(key=lambda x: x[1], reverse=True)

#print(*comps)

summ = 0
for comp in comps:
    summ += comp[1]

for i in range(m):
    comps[i][1] = n * comps[i][1] / summ

#print(*comps)

tasks = n
for i in range(m):
    if tasks - ceil(comps[i][1]) >= 0:
        comps[i][1] = ceil(comps[i][1])
    else:
        comps[i][1] = max(tasks, 0)
    tasks -= int(comps[i][1] + 0.5)

#print(*comps)

comps.sort(key=lambda x: x[0])

#print(*comps)

answer = []
for comp in comps:
    answer.append(comp[1])

total_time = float('-inf')
for i in range(m):
    nn = answer[i]
    t, b, y = for_answer[i]
    if nn % b != 0:
        total_time = max(total_time, (nn // b) * (t * b + y) + nn % b)
    else:
        total_time = max(total_time, (nn // b) * (t * b + y) - y)

print(total_time)
print(*answer)
