import sys


def dfs(s: tuple[int, int], t: tuple[int, int], field: list[str], visited: list[list[bool]]) -> dict:
    stack = [s]

    parents = {s: None}
    visited[s[1]][s[0]] = True
    while stack:
        current = stack.pop()

        if current == t:
            return parents

        col, row = current
        for dc, dr in ((0, -1), (-1, 0), (1, 0), (0, 1)):
            new_c, new_r = col + dc, row + dr
            if field[new_r][new_c] == "." and not visited[new_r][new_c]:
                visited[new_r][new_c] = True
                parents[(new_c, new_r)] = current
                stack.append((new_c, new_r))


def traceback(s: tuple[int, int], t: tuple[int, int], parents: dict) -> list:
    path = []
    curr = t
    while curr is not None:
        path.append(curr)
        curr = parents[curr]
    path.reverse()
    return path


def main() -> None:
    w, h, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    field = ["*" * (w + 2)]
    for _ in range(h):
        field.append("*" + sys.stdin.readline().strip() + "*")
    field.append("*" * (w + 2))

    s, t = (x1, y1), (x2, y2)
    visited = [[False for _ in range(w + 2)] for _ in range(h + 2)]

    parents = dfs(s, t, field, visited)
    del field
    del visited
    if parents:
        print("YES")
        for dot in traceback(s, t, parents):
            print(*dot)
    else:
        print("NO")


if __name__ == "__main__":
    main()
