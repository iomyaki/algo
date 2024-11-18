from collections import deque


class ZigzagIterator:
    def __init__(self, lists: list) -> None:
        self.lists = lists
        self.queue = deque()
        for i in range(len(self.lists)):
            self.queue.append((0, i))

    def next(self) -> int:
        now, lst = self.queue.popleft()

        if now != len(self.lists[lst]) - 1:
            self.queue.append((now + 1, lst))

        return self.lists[lst][now]

    def has_next(self) -> deque:
        return self.queue


def main():
    lists = []
    for _ in range(int(input())):
        lists.append(tuple(map(int, input().split())))

    zigzag_iterator = ZigzagIterator(lists)
    while zigzag_iterator.has_next():
        print(zigzag_iterator.next(), end=" ")


if __name__ == "__main__":
    main()


# не тратится дополнительная память на хранение списков или итераторов
# масштабируемо для разных k (не только для k = 2)
