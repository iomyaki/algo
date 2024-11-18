def two_sum(nums: list[int], target: int):
    visited = {}
    for idx in range(len(nums)):
        num = nums[idx]
        complement = target - num
        if complement in visited:
            return [visited[complement], idx]

        visited[num] = idx

    return [-1, -1]


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
