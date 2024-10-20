# https://www.geeksforgeeks.org/number-of-longest-increasing-subsequences/

def RANKER(nums):
    # Rank the elements in the array from 0 to n-1 based on their values,
    # returns the number of distinct elements in the array.
    n = len(nums)
    temp = nums.copy()
    temp.sort()
    rank = {}
    mx = 0
    for i in range(n):
        if temp[i] not in rank:
            rank[temp[i]] = mx
            mx += 1
    for i in range(n):
        nums[i] = rank[nums[i]]
    return mx


def chooseBest(left, right):
    # Given two pairs, return the pair that has the longer maximum length,
    # and if they have the same maximum length, add their ways together.
    mxLen_LFT, ways_LFT = left
    mxLen_RHT, ways_RHT = right
    if mxLen_LFT > mxLen_RHT:
        res = (mxLen_LFT, ways_LFT)
    elif mxLen_LFT < mxLen_RHT:
        res = (mxLen_RHT, ways_RHT)
    else:
        res = (mxLen_LFT, ways_LFT + ways_RHT)
    return res


def update(start, end, parent, element, mxLength, ways, tree):
    # Update the segment tree to reflect the new element added to the array.
    if start == end:
        if tree[parent][0] == mxLength:
            tree[parent] = (mxLength, tree[parent][1] + ways)
        else:
            tree[parent] = (mxLength, ways)
        return
    mid = (start + end) // 2
    if element <= mid:
        update(start, mid, 2 * parent + 1, element, mxLength, ways, tree)
    else:
        update(mid + 1, end, 2 * parent + 2, element, mxLength, ways, tree)
    tree[parent] = chooseBest(tree[2 * parent + 1], tree[2 * parent + 2])


def maxLen(start, end, qstart, qend, parent, tree):
    # Given the range qstart to qend, return the pair with the longest maximum length.
    if start > qend or end < qstart:
        return (0, 0)
    if start >= qstart and end <= qend:
        return tree[parent]
    mid = (start + end) // 2
    left = maxLen(start, mid, qstart, qend, 2 * parent + 1, tree)
    right = maxLen(mid + 1, end, qstart, qend, 2 * parent + 2, tree)
    return chooseBest(left, right)


def findNumberOfLIS(nums):
    # Given an array, find the number of longest increasing subsequences.
    n = len(nums)
    mx = RANKER(nums)
    tree = [(0, 0)] * (4 * mx + 5)
    for i in range(n):
        # initialize the max length and ways for this element
        mxLen = 1
        ways = 1
        if nums[i] > 0:  # if nums[i] is not the first element
            info = maxLen(0, mx, 0, nums[i] - 1, 0, tree)
            if info[0] + 1 > mxLen:
                mxLen = info[0] + 1
                ways = info[1]
        update(0, mx, 0, nums[i], mxLen, ways, tree)
    return tree[0][1]


n = int(input())
lst = list(map(int, input().split()))

print(findNumberOfLIS(lst) % (10 ** 9 + 7))
