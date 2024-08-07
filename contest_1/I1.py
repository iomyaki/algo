n = int(input())
variants = tuple(map(int, input().split()))

print(1, end=' ')

mapa = {i: 0 for i in variants}
mapa[0] = 0

C1_K = n
C1 = 0
for i in variants:
    mapa[i] = 1
    C1 += 1

    if i == C1_K:
        while mapa[C1_K] == 1:
            C1_K -= 1

    print(C1 - (n - C1_K) + 1, end=' ')
