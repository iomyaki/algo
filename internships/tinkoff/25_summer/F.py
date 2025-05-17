import heapq
import sys


def get_best_pref(n: int, arr: list[int]) -> list[int]:
    prefix = [0 for _ in range(n + 1)]
    low, high = [], []
    sum_low, total = 0, 0

    for i in range(1, n + 1):
        val = arr[i - 1]
        total += val
        if not low or val <= -low[0]:
            heapq.heappush(low, -val)
            sum_low += val
        else:
            heapq.heappush(high, val)

        half = i // 2
        while len(low) > half:
            val = -heapq.heappop(low)
            sum_low -= val
            heapq.heappush(high, val)
        while len(low) < half and high:
            val = heapq.heappop(high)
            sum_low += val
            heapq.heappush(low, -val)

        if low and high:
            low_top = -low[0]
            high_top = high[0]
            if low_top > high_top:
                top_low = -heapq.heappop(low)
                top_high = heapq.heappop(high)
                sum_low += (top_high - top_low)
                heapq.heappush(low, -top_high)
                heapq.heappush(high, top_low)

        if i % 2 == 0:
            prefix[i] = total - 2 * sum_low

    return prefix


def main():
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().split()))

    if n % 2 == 0:
        mid = n // 2
        arr.sort()
        print(sum(arr[mid:]) - sum(arr[:mid]))
    else:
        prefix = get_best_pref(n, arr)
        suffix = get_best_pref(n, arr[::-1])[::-1]
        answer = -float('inf')
        for i in range(0, n, 2):
            current = prefix[i] + suffix[i + 1]
            if current > answer:
                answer = current
        print(answer)


if __name__ == '__main__':
    main()
