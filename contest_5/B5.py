# Rabin–Karp algorithm

def find_substring(t, s, base=31, modulus=int(1e9 + 7)):
    len_t = len(t)
    len_s = len(s)
    hash_t = 0  # hash value for txt
    hash_s = 0  # hash value for pattern
    base_pow = 1
    findings = []
    #r = 0  # in case of collisions

    if len_s > len_t:
        return [0]

    # The value of base_pow would be "pow(base, len_s - 1) % mod"
    for _ in range(len_s - 1):
        base_pow = (base_pow * base) % modulus

    # Calculate the hash value of pattern and first window of the text
    for i in range(len_s):
        hash_t = (base * hash_t + (ord(t[i]) - ord('a') + 1)) % modulus
        hash_s = (base * hash_s + (ord(s[i]) - ord('a') + 1)) % modulus

    # Slide the pattern over text one by one
    for i in range(len_t - len_s + 1):
        # Check the hash values of current window of text and pattern if the hash values match then only check
        # for characters one by one
        if hash_s == hash_t:
            # Check for characters one by one
            #for r in range(len_s):
                #if tree[i + r] != s[r]:
                    #break

            #r += 1
            # if hash_s == hash_t and s[0...len_s-1] = tree[i, i + 1, ...i + len_s-1]
            #if r == len_s:
            findings.append(i)
            #print("Pattern found at index " + str(i))

        # Calculate hash value for next window of text: Remove leading digit, add trailing digit
        if i < len_t - len_s:
            hash_t = (base * (hash_t - (ord(t[i]) - ord('a') + 1) * base_pow) + (ord(t[i + len_s]) - ord('a') + 1)) % modulus

            # We might get negative values of tree, converting it to positive
            #if hash_t < 0:
                #hash_t = hash_t + mod

    return len(findings), *findings


t = input()
for _ in range(int(input())):
    print(*find_substring(t, input()))
