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
        for j in range(p + 2, n + 1, 2):
            if sieve[j]:
                p = j
                break

    # collect all remaining prime numbers
    for i in range(prime[-1] + 1, n + 1):
        if sieve[i]:
            prime.append(i)

    return prime


def main():
    n = int(input())
    prime = sieve_of_Eratosthenes(n)
    prime_set = set(prime)
    for p in prime:
        diff = n - p
        if diff in prime_set:
            print(p, diff)
            break


if __name__ == '__main__':
    main()
