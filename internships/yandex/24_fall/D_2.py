def is_matching(opn: str, cls: str) -> bool:
    return opn == "(" and cls == ")" or opn == "[" and cls == "]" or opn == "{" and cls == "}"


def count_valid_sequences(s: str) -> int:
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    opening = {"(", "[", "{"}
    closing = {")", "]", "}"}

    for i in range(n - 1):
        j = i + 1
        if s[i] == s[j] == "?":
            dp[i][j] = 3
        elif s[i] == "?" and s[j] in closing or s[i] in opening and s[j] == "?" or is_matching(s[i], s[j]):
            dp[i][j] = 1

    for length in range(4, n + 1, 2):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] in closing or s[j] in opening:
                continue
            else:
                count = 0

                if s[i] == s[j] == "?":
                    indicator = 3
                elif s[i] == "?" and s[j] in closing or s[i] in opening and s[j] == "?" or is_matching(s[i], s[j]):
                    indicator = 1
                else:
                    indicator = 0
                count += indicator * dp[i + 1][j - 1]

                """for k in range(i + 1, j, 2):
                    count += dp[i][k] * dp[k + 1][j]"""

                max_var = -1
                for k in range(i + 1, j, 2):
                    max_var = max(max_var, dp[i][k] * dp[k + 1][j])
                count += max_var

                dp[i][j] = count

    return dp[0][-1]


#seq = "?{?[(?])?)"
#seq = "[]()"
#seq = "]??("
#seq = "[]??()"
#seq = "????????"  # ???? - answer: 18
#seq = "?[?]??"
#seq = "{}????()"  # answer: 18
#print(count_valid_sequences(seq))
print(count_valid_sequences("??????"))
assert count_valid_sequences("?{?[(?])?)") == 3
assert count_valid_sequences("[]()") == 1
assert count_valid_sequences("]??(") == 0
assert count_valid_sequences("[]??()") == 3
assert count_valid_sequences("????") == 18
assert count_valid_sequences("?[?]??") == 6
assert count_valid_sequences("{}????()") == 18
