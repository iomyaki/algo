_, m = map(int, input().split())
prices = tuple(map(int, input().split()))

remains = []
for i in range(m + 1):
    money = i
    for n in prices:
        if n <= money:
            money -= n
    remains.append(money)

print(max(remains))
