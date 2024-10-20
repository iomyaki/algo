a = input()
b = input()
bb = b * 2

base = 67
modulus = int(1e9 + 7)
base_pow = 1

len_a, len_b = len(a), len(b)
hash_a, hash_b = 0, 0
shifts = set()

for _ in range(len_b - 1):
    base_pow = (base_pow * base) % modulus

for i in range(len_b):
    hash_a = (base * hash_a + ord(a[i])) % modulus
    hash_b = (base * hash_b + ord(b[i])) % modulus
shifts.add(hash_b)

for i in range(len_b):
    if i < len_b - 1:
        hash_b = (base * (hash_b - ord(bb[i]) * base_pow) + ord(bb[i + len_b])) % modulus
        shifts.add(hash_b)

counter = 0
if hash_a in shifts:
    counter += 1

for i in range(len_a - len_b + 1):
    if i < len_a - len_b:
        hash_a = (base * (hash_a - ord(a[i]) * base_pow) + ord(a[i + len_b])) % modulus
        if hash_a in shifts:
            counter += 1

print(counter)
