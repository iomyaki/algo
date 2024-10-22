n = int(input())

for i in range(n):
    _ = input()
    degrees = list(map(int, input().split()))
    if sum(degrees) % 2 == 0:
        print('Yes')
    else:
        print('No')
