_, _ = map(int, input().split())
numbers = list(map(int, input().split()))
questions = list(map(int, input().split()))

for q in questions:
    le = 0
    r = len(numbers) - 1
    while le != r - 1:
        mid = (le + r) // 2

        if numbers[mid] < q:
            le = mid
        elif numbers[mid] > q:
            r = mid
        else:
            print('YES')
            break
    else:
        if numbers[le] == q or numbers[r] == q:
            print('YES')
        else:
            print('NO')
