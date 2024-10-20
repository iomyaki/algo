from collections import deque


def main():
    target = input()
    k = int(input())
    n = int(input())

    graph = {}
    for _ in range(n):
        fr, to = input().split()
        if fr in graph:
            graph[fr].add(to)
        else:
            graph[fr] = {to}
        graph[to] = set()

    # breadth-first search in orgraph
    visited = {"LED"}
    start = ("LED", -1)
    queue = deque([start])
    while queue:
        v = queue.popleft()

        if v[0] == target:
            if v[1] <= k:
                print(v[1])
            else:
                print("impossible")
            break

        if v not in visited:
            visited.add(v[0])
            for u in graph[v[0]]:
                if u not in visited:
                    queue.append((u, v[1] + 1))
    else:
        print("impossible")


if __name__ == "__main__":
    main()

"""
Tests:

TGT
5
7
LED D
D C
C TGT
LED A
A B
B C
LED C

TGT
1
11
LED TGT
TGT LED
LED A
A TGT
A B
B TGT
B C
A D
D E
E TGT
E B

TGT
3
10
LED A
LED E
E A
A B
B C
E F
F C
C D
D TGT
A E

TGT
5
10
LED A
LED E
E A
A B
B C
E F
F C
C D
D TGT
A E

TGT
2
5
LED A
LED B
A D
A C
B C

TGT
1
4
LED A
LED B
A B
B TGT

TGT
1
4
LED B
LED A
B A
A TGT

TGT
1
12
LED TGT
TGT LED
LED A
A TGT
A B
B A
B TGT
B C
A D
D E
E TGT
E B
"""