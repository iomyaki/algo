n, s = tuple(map(int, input().split(' ')))
prices = list(map(int, input().split(' ')))

prices.sort()

last = ''

if s < prices[0]:
    print(0)
else:
    for i in range(n):
        if s < prices[i]:
            last = prices[i - 1]
            print(prices[i - 1])
            break

    if last == '':
        print(prices[-1])