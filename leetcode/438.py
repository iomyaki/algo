class Solution:
    def find_anagrams(self, s: str, p: str) -> list[int]:
        anagrams = []

        # get lengths of strings
        n, m = len(p), len(s)

        # if s is shorter than p, it can't contain anagrams of p
        if m < n:
            return anagrams

        # fill a dictionary with symbols from p
        dct = {}
        for c in p:
            dct[c] = dct.get(c, 0) + 1

        # mutually destroy symbols from p with symbols from s
        for i in range(n):
            c = s[i]
            dct[c] = dct.get(c, 0) - 1
            if dct[c] == 0:
                del dct[c]

        if dct == {}:
            anagrams.append(0)

        for i in range(n, m):
            ind_out = i - n
            ind_in = i
            c_out = s[ind_out]
            c_in = s[ind_in]

            dct[c_out] = dct.get(c_out, 0) + 1
            dct[c_in] = dct.get(c_in, 0) - 1
            if dct[c_out] == 0:
                del dct[c_out]
            if c_in != c_out and dct[c_in] == 0:
                del dct[c_in]

            if dct == {}:
                anagrams.append(i - n + 1)

        return anagrams
