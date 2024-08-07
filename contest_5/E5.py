def find_substring(t, s, base=67, modulus=int(1e9 + 7)):
    len_t = len(t)
    len_s = len(s)

    if len_s > len_t:
        return 0
    elif len_s == len_t:
        mismatches = 0
        for i in range(len_s):
            if t[i] != s[i]:
                mismatches += 1
            if mismatches > 1:
                return 0
        return 1, [1]

    hash_t = 0
    base_pow = 1
    findings = []
    variations = set()

    for _ in range(len_s - 1):
        base_pow = (base_pow * base) % modulus

    for i in range(len_s):
        hash_t = (base * hash_t + ord(t[i])) % modulus

    letters = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    for letter in letters:
        for j in range(len_s):
            hash_s = 0
            for i in range(len_s):
                if i == j:
                    hash_s = (base * hash_s + ord(letter)) % modulus
                else:
                    hash_s = (base * hash_s + ord(s[i])) % modulus
            variations.add(hash_s)

    for i in range(len_t - len_s + 1):
        if hash_t in variations:
            findings.append(i + 1)

        if i < len_t - len_s:
            hash_t = (base * (hash_t - ord(t[i]) * base_pow) + ord(t[i + len_s])) % modulus

    return len(findings), findings


s = input()
t = input()

answer = find_substring(t, s)
if answer == 0:
    print(0)
else:
    print(answer[0])
    print(*answer[1])
