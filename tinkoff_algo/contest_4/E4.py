def check(x):
    sum = 0
    count = 1
    for i in range(n):
        sum += arr[i]
        if sum > x:
            count += 1
            sum = arr[i]
        if count > k:
            return False
    return True


n, k = map(int, input().split())
arr = tuple(map(int, input().split()))

maxSum = 0
minSum = max(arr)

for i in range(n):
    maxSum += arr[i]

ans = 0
while minSum <= maxSum:
    mid = (minSum + maxSum) // 2
    if check(mid):
        ans = mid
        maxSum = mid - 1
    else:
        minSum = mid + 1

print(ans)
