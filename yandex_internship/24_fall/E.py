import sys


class TrieNode:
    def __init__(self, parent=None) -> None:
        self.parent = parent
        self.children = {}
        self.containing = {}
        self.end = -1


class Trie:
    def __init__(self, n: int) -> None:
        self.root = TrieNode()
        self.n = n

    def insert(self, word: str, idx: int) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(node)
            node = node.children[c]
            node.containing[idx] = len(node.containing) + 1
        node.end = idx

    def count_actions(self, query: str) -> int:
        cnt = 0
        # спуститься из корня
        node = self.root
        for c in query:
            if c in node.children:
                node = node.children[c]
            else:
                break

        # подняться в корень
        if node.end != -1:
            idx = node.end
            while node.parent is not None:
                cnt += node.containing[idx]  # посчитать префиксы
                node = node.parent
            cnt += idx + 1  # посчитать слова
        else:
            while node.parent is not None:
                cnt += len(node.containing)  # посчитать префиксы
                node = node.parent
            cnt += self.n  # посчитать слова

        return cnt


def main() -> None:
    n = int(sys.stdin.readline())
    bor = Trie(n)
    for i in range(n):
        bor.insert(sys.stdin.readline().rstrip(), i)
    for _ in range(int(sys.stdin.readline())):
        print(bor.count_actions(sys.stdin.readline().rstrip()))


if __name__ == "__main__":
    main()
