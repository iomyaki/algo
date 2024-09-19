from collections import deque


def main():
    n = int(input())
    queue = deque([])
    goods = {a: 0 for a in range(1, 10001)}
    for _ in range(n):
        typ, t, a = map(int, input().split())
        if typ == 1:
            goods[a] += 1
        else:
            queue.append((a, t))

        while len(queue) > 0 and goods[queue[0][0]] > 0:
            print(t - queue[0][1], end=" ")
            goods[queue[0][0]] -= 1
            queue.popleft()

    if len(queue) > 0:
        for _ in range(len(queue)):
            print(-1, end=" ")


if __name__ == "__main__":
    main()
