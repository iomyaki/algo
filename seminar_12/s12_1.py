import random
import sys
import time


def naive_gcd(a, b):
    """
    Time complexity: O(max(a, b))
    """
    if a < b:
        a, b = b, a

    if b == 0:
        return a
    else:
        return naive_gcd(b, a - b)


def gcd(a, b):
    """
    Time complexity: O(log(min(a, b)))
    """
    while b > 0:
        a %= b
        a, b = b, a

    return a


def check_working_time(alg, mode):
    numbers = [n for n in range(50000000, 100000000)]
    ts = []
    if mode == 'usual':
        if alg == 'naive_gcd':
            for _ in range(1000000):
                start = time.time()
                naive_gcd(random.choice(numbers), random.choice(numbers))
                ts.append(time.time() - start)

            return sum(ts) / 1000000
        elif alg == 'gcd':
            for _ in range(1000000):
                start = time.time()
                gcd(random.choice(numbers), random.choice(numbers))
                ts.append(time.time() - start)

            return sum(ts) / 1000000
    elif mode == 'fib':
        if alg == 'naive_gcd':
            for _ in range(1000000):
                start = time.time()
                naive_gcd(1.6602747662452085e208, 2.686381002448534e208)
                ts.append(time.time() - start)

            return sum(ts) / 1000000
        elif alg == 'gcd':
            for _ in range(1000000):
                start = time.time()
                gcd(1.6602747662452085e208, 2.686381002448534e208)
                ts.append(time.time() - start)

            return sum(ts) / 1000000


sys.setrecursionlimit(10 ** 9)
random.seed(42)

print(f'naive_gcd avg working time (random): {check_working_time("naive_gcd", "usual")}')
print(f'gcd avg working time (random): {check_working_time("gcd", "usual")}')
print()
print(f'naive_gcd avg working time (Fib.): {check_working_time("naive_gcd", "fib")}')  # 100 iterations
print(f'gcd avg working time (Fib.): {check_working_time("gcd", "fib")}')  # 55 iterations
