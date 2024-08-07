from collections import deque


def main():
    k = int(input())
    n = int(input())

    graph = {}
    for _ in range(n):
        fr, to = input().split()
        if fr in graph:
            graph[fr].add(to)
        else:
            graph[fr] = {to}
        if to not in graph:
            graph[to] = set()

    depths = {v: -1 for v in graph}
    depths["S"] = 0

    queue = deque(["S"])
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if depths[w] == -1:
                queue.append(w)
                depths[w] = depths[v] + 1
            elif w == "S":
                path = depths[v] + 1
                if path <= k:
                    print(path)
                else:
                    print("impossible")
                return
    else:
        print("impossible")


if __name__ == "__main__":
    main()

"""
Tests:

2
5
S A
A D
A B
B C
C A

3
8
S A
S D
A E
A B
E F
F B
B C
C S

6
8
S A
S D
A E
A B
E F
F B
B C
C S

3
4
A B
B C
B S
C A
"""