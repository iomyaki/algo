import sys
from collections import deque

MOVES = {(1, 0): "d", (-1, 0): "u", (0, 1): "r", (0, -1): "l"}


def check_correct(x: int, y: int, graph: list[str]) -> bool:
    n = len(graph)
    return 0 <= x < n and 0 <= y < n and graph[x][y] != "#"


def bfs(graph: list[str], player: tuple[int, int], box: tuple[int, int], target: tuple[int, int]) -> str | int:
    visited = {(player[0], player[1], box[0], box[1])}

    queue = deque([(player[0], player[1], box[0], box[1], "")])
    while queue:
        player_x, player_y, box_x, box_y, moves = queue.popleft()

        if (box_x, box_y) == target:
            return moves

        for (dx, dy), move in MOVES.items():
            new_player_x, new_player_y = player_x + dx, player_y + dy

            if (new_player_x, new_player_y) == (box_x, box_y):
                new_box_x, new_box_y = box_x + dx, box_y + dy

                if check_correct(new_box_x, new_box_y, graph) and (new_player_x, new_player_y, new_box_x, new_box_y) not in visited:
                    visited.add((new_player_x, new_player_y, box_x, box_y))
                    queue.append((new_player_x, new_player_y, new_box_x, new_box_y, moves + move.upper()))
            else:
                if check_correct(new_player_x, new_player_y, graph) and (new_player_x, new_player_y, box_x, box_y) not in visited:
                    visited.add((new_player_x, new_player_y, box_x, box_y))
                    queue.append((new_player_x, new_player_y, box_x, box_y, moves + move))

    return -1


def main() -> None:
    n = int(sys.stdin.readline())
    graph = [sys.stdin.readline().rstrip() for _ in range(n)]

    player, box, target = None, None, None
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "s":
                player = (i, j)
            elif graph[i][j] == "*":
                box = (i, j)
            elif graph[i][j] == "+":
                target = (i, j)

    moves = bfs(graph, player, box, target)
    if moves == -1:
        print(-1)
    else:
        print(len(moves))
        print(moves)


if __name__ == "__main__":
    main()
