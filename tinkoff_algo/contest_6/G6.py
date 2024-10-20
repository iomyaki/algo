n, m = map(int, input().split())
graph = [[float('inf') for _ in range(n)] for _ in range(n)]
for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    a, b, length = map(int, input().split())
    graph[a - 1][b - 1] = length
    graph[b - 1][a - 1] = length

#print(*graph, sep='\n')
#print('-------------------------')

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

#print(*graph, sep='\n')
#print('-------------------------')

maxs = []
for node in graph:
    maxs.append(max(node))

#print(maxs)
#print(min(maxs))
print(maxs.index(min(maxs)) + 1)
