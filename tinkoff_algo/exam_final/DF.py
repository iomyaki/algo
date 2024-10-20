def sieve_of_Eratosthenes(n):
    sieve = [True for _ in range(n + 1)]
    prime = [2]

    # zero and one are not prime numbers
    sieve[0], sieve[1] = False, False

    # cross out all even numbers except two
    for i in range(4, n + 1, 2):
        sieve[i] = False

    p = 3
    while p ** 2 <= n:
        # add the current number (p) to the list of primes
        prime.append(p)

        # cross out all numbers containing the current (p) as a factor
        for i in range(p ** 2, n + 1, p * 2):
            sieve[i] = False

        # find the next prime number
        for j in range(p + 1, n + 1):
            if sieve[j]:
                p = j
                break

    # collect all remaining prime numbers
    for i in range(prime[-1] + 1, n + 1):
        if sieve[i]:
            prime.append(i)

    return prime


def dfs(v):
    global depth, variants

    if depth == n - 2:
        variants += 1
        variants = variants % mod
    else:
        for w in graph[v][0]:
            if w not in used:
                depth += 1
                dfs(w)

    depth -= 1


n = int(input())
mod = 10 ** 9 + 9
variants = 0

prime3dig = sieve_of_Eratosthenes(999)[25:]
graph = {}
for first_prime in prime3dig:
    graph[first_prime] = [[], None]
    first_element = first_prime % 100
    for second_prime in prime3dig:
        second_element = second_prime // 10
        if first_element == second_element:
            graph[first_prime][0].append(second_prime)

for prime in prime3dig:
    depth = 1
    used = set()
    dfs(prime)

print(variants % mod)

# TL test 7
