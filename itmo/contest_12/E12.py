import sys
from collections import deque

MOVES = ((-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2))


def check_correct(x: str, y: str) -> bool:
    return "a" <= x <= "h" and 1 <= int(y) <= 8


def bfs(start: str) -> dict:
    visited = {start}
    ancestors = {start: None}

    queue = deque([start])
    while queue:
        state = queue.popleft()
        for i in range(8):
            dx, dy = MOVES[i]

            x1, y1 = chr(ord(state[0]) + dx), str(int(state[1]) + dy)
            turn1 = x1 + y1 + state[2:]
            if check_correct(x1, y1) and turn1 not in visited and (x1 != state[2] or y1 != state[3]):
                visited.add(turn1)
                ancestors[turn1] = state
                queue.append(turn1)

            x2, y2 = chr(ord(state[2]) + dx), str(int(state[3]) + dy)
            turn2 = state[:2] + x2 + y2
            if check_correct(x2, y2) and turn2 not in visited and (x2 != state[0] or y2 != state[1]):
                visited.add(turn2)
                ancestors[turn2] = state
                queue.append(turn2)

    return ancestors


def traceback(ancestors: dict, final: str) -> None:
    path = []
    current = final
    while current is not None:
        path.append(current)
        current = ancestors[current]

    for i in range(len(path) - 2, -1, -1):
        prev = path[i + 1]
        curr = path[i]

        if prev[0] != curr[0] or prev[1] != curr[1]:
            print(f"1 {curr[0]}{curr[1]}")
        else:
            print(f"2 {curr[2]}{curr[3]}")


def main() -> None:
    start_1 = sys.stdin.readline().rstrip()
    start_2 = sys.stdin.readline().rstrip()
    finish_1 = sys.stdin.readline().rstrip()
    finish_2 = sys.stdin.readline().rstrip()

    initial = start_1 + start_2
    final = finish_1 + finish_2

    traceback(bfs(initial), final)


if __name__ == "__main__":
    main()
