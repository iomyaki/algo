import heapq
import sys


class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def main() -> None:
    def get_codes(node: Node, curr: str, codes: dict) -> None:
        if node is not None:
            if node.char is not None:
                codes[node.char] = curr
            get_codes(node.left, curr + "0", codes)
            get_codes(node.right, curr + "1", codes)

    s = sys.stdin.readline().rstrip()
    n = len(s)

    if len(set(s)) == 1:
        print(f"1 {n}\n{s[0]}: {0}\n{'0' * n}")
        return

    # count frequencies
    freqs = {}
    for char in s:
        freqs[char] = freqs.get(char, 0) + 1

    # build the trie
    heap = [Node(char, freq) for char, freq in freqs.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left_child = heapq.heappop(heap)
        right_child = heapq.heappop(heap)
        merged_node = Node(freq=left_child.freq + right_child.freq)
        merged_node.left = left_child
        merged_node.right = right_child
        heapq.heappush(heap, merged_node)

    # generate codes
    Haffman_codes = {}
    get_codes(heap[0], "", Haffman_codes)

    # answer
    encoded_s = []
    for char in s:
        encoded_s.append(Haffman_codes[char])
    encoded_s = "".join(encoded_s)

    print(len(Haffman_codes), len(encoded_s))
    for char, code in Haffman_codes.items():
        print(f"{char}: {code}")
    print(encoded_s)


if __name__ == "__main__":
    main()
