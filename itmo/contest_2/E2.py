from collections import deque


def main():
    _, k = map(int, input().split())
    numbers = deque(list(map(int, input().split())))
    mod = 2 ** 30
    for _ in range(k):
        x, y = numbers[0], numbers[-1]
        if x < y:
            numbers.popleft()
            numbers.append((x + y) % mod)
        else:
            numbers.pop()
            numbers.appendleft((y - x) % mod)
    print(*numbers)


if __name__ == "__main__":
    main()

# TL
