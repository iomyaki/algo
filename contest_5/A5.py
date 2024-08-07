def get_base_powers(limit=int(1e5 + 5), base=31, modulus=int(1e9 + 7)):
    base_powers = [0] * limit
    base_powers[0] = 1

    for i in range(1, limit):
        base_powers[i] = (base_powers[i - 1] * base) % modulus

    return base_powers


def str2nums(string):
    numbers = []
    for letter in string:
        numbers.append(ord(letter) - ord('a') + 1)

    return numbers


def get_hash_values(string, limit=int(1e5 + 5), base=31, modulus=int(1e9 + 7)):
    numbers = str2nums(string)
    base_powers = get_base_powers(limit=limit, base=base, modulus=modulus)

    hash_list = [0] * limit
    for i in range(len(numbers)):
        hash_list[i + 1] = (hash_list[i] + base_powers[i] * numbers[i]) % modulus

    return hash_list


s = input()
m = int(input())
n = int(1e5)
mod = int(1e9 + 7)

bases = get_base_powers()
hashes = get_hash_values(s)

for _ in range(m):
    a, b, c, d = map(lambda x: x - 1, map(int, input().split()))
    if (hashes[b + 1] - hashes[a]) * bases[n - a] % mod == (hashes[d + 1] - hashes[c]) * bases[n - c] % mod:
        print('Yes')
    else:
        print('No')
