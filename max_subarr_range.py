from collections import deque


def main():
    """
    Given an array of integer numbers, find the maximum sum
    of the elements in a contiguous subarray having a length between a and b
    """

    n, a, b = map(int, input().split())
    arr = list(map(int, input().split()))

    pref = [arr[0]]
    for i in range(1, n):
        pref.append(arr[i] + pref[-1])

    d = b - a
    queue = deque()
    answer = float("-inf")
    for i in range(a, n + d + 1):
        if queue and queue[0][1] < i - d:
            queue.popleft()
        if i < n:
            while queue and queue[-1][0] <= pref[i]:
                queue.pop()
            queue.append((pref[i], i))
        if queue and i >= b:
            answer = max(answer, queue[0][0] - pref[i - b])

    print(answer)


if __name__ == "__main__":
    main()
