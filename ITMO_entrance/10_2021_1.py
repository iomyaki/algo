"""
[1] -> 0 (и любое другое число)
[1, 2] -> 0 (и любое количество попарно разных чисел)
[1, 1, 2] -> 1
[5, 2, 1, 5, 7, 6, 8, 1, 5, 10] -> 2
"""

arr = list(map(int, input().split()))

counts = {}
for n in arr:
    counts[n] = counts.get(n, 0) + 1

high_count = max(counts.values())
low_count = min(counts.values())

print(high_count - low_count)
