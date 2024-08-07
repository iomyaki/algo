def get_polynomial_hash(string, base=31, modulus=int(1e9 + 7)):
    hash_value = 0
    base_power = 1
    for c in string:
        x = ord(c) - ord('a') + 1
        hash_value = (hash_value + base_power * x) % modulus
        base_power = (base_power * base) % modulus

    return hash_value


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
    """
    prefix hashes
    """

    numbers = str2nums(string)
    base_powers = get_base_powers(limit=limit, base=base, modulus=modulus)

    hash_list = [0] * limit
    for i in range(len(numbers)):
        hash_list[i + 1] = (hash_list[i] + base_powers[i] * numbers[i]) % modulus

    return hash_list


class HashTable:
    def __init__(self):
        self.size = int(1e9 + 7)
        self.data = [[] for _ in range(self.size)]

    def hash(self, elem, base=67, modulus=int(1e9 + 7)):
        hash_value = 0
        base_power = 1
        for c in elem:
            x = ord(c)
            hash_value = (hash_value + base_power * x) % modulus
            base_power = (base_power * base) % modulus

        return hash_value

    def insert(self, elem):
        self.data[self.hash(elem)].append(elem)

    def find(self, elem):
        for x in self.data[self.hash(elem)]:
            if x == elem:
                return True

        return False
