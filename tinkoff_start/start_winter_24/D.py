n, k = map(int, input().split())

companies = set()
for _ in range(k):
    companies.add(input())

values = {}
graph = {0: [None, []]}
# graph structure: {vertex: [its parent, [its child, its_child, ...]]}
for i in range(1, n + 1):
    info = input().split()
    values[i] = (int(info[1]), info[2])  # save price and company type

    if i not in graph:  # it could have been added as someone's parent previously
        graph[i] = [int(info[0]), []]
    else:
        graph[i][0] = int(info[0])

    if int(info[0]) not in graph:
        graph[int(info[0])] = [None, []]  # if the parent of the current vertex not in graph, then add it

    graph[int(info[0])][1].append(i)  # extend the list of children of the parent of the current node

del graph[0]  # delete the service vertex number zero


def descend(parent):
    global from_child
    global companies_found
    global cost

    companies_found.add(values[parent][1])
    cost += values[parent][0]

    for child in graph[parent][1]:  # recursively calculate the whole subtree of this parent
        if child != from_child:  # except of the vertex we came from
            descend(child)


# if there has been a transition to the parent, there's no need to make the same transition again —
# as the corresponding subtree has already been inspected
already_passed = []
all_costs = []
for vertex in graph:
    if len(graph[vertex][1]) == 0:  # we will ascend from final vertices ("leafs")
        companies_found = {values[vertex][1]}
        cost = values[vertex][0]
        current = vertex
        while current:  # in this loop, we always go to the parent of the previous vertex
            if graph[current][0] not in already_passed:
                already_passed.append(graph[current][0])
                from_child = current
                current = graph[current][0]  # ascending — transition to the parent
            else:
                break

            descend(current)  # here we inspect a subtree of this parent

            if companies_found & companies == companies:  # because there can be other companies than interesting ones
                all_costs.append(cost)
                break

            if current == 1:  # if we've reached the root and none of the above is true, this tree can'tree be solved
                break

if len(all_costs) != 0:
    print(min(all_costs))
else:
    print(-1)

"""
5 2
A
B
0 1 A
1 2 A
1 2 B
1 1 B
4 2 A
answer: 3
------
16 3
A
B
C
0 1 A
1 1 B
2 1 A
2 2 D
6 1 D
7 1 C
1 1 B
10 1 B
10 1 A
1 2 B
1 2 D
11 1 B
12 1 A
12 1 A
14 1 C
14 1 B
answer: 3
"""
