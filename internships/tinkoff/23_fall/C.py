n = int(input())
Joe = input().replace(' ', '')
win = input().replace(' ', '')

newJoe = newWin = ''

for i in range(n):
    if Joe[i] != win[i]:
        newJoe += Joe[i]
        newWin += win[i]

if ''.join(sorted(newJoe)) == newWin:
    print('YES')
else:
    print('NO')
