n, q = map(int, input().split())
numbers = list(map(int, input().split()))

for _ in range(q):
    query = input().split()
    if query[0] == '+':
        for i in range(int(query[1]) - 1, int(query[2])):
            numbers[i] += int(query[3])
    else:
        results = []
        for i in range(int(query[1]) - 1, int(query[2])):
            results.append(min(numbers[i], int(query[3]) * (i + 1) + int(query[4])))
        print(max(results))
