class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:
        # get lengths of strings
        n, m = len(s1), len(s2)

        # if s2 is shorter than s1, it can't contain anagrams of s1
        if m < n:
            return False

        # fill a dictionary with symbols from s1
        dct = {}
        for c in s1:
            dct[c] = dct.get(c, 0) + 1

        # mutually destroy symbols from s1 with symbols from s2
        for i in range(n):
            c = s2[i]
            dct[c] = dct.get(c, 0) - 1
            if dct[c] == 0:
                del dct[c]

        if dct == {}:
            return True

        for i in range(n, m):
            ind_out = i - n
            ind_in = i
            c_out = s2[ind_out]
            c_in = s2[ind_in]

            dct[c_out] = dct.get(c_out, 0) + 1
            dct[c_in] = dct.get(c_in, 0) - 1
            if dct[c_out] == 0:
                del dct[c_out]
            if c_in != c_out and dct[c_in] == 0:
                del dct[c_in]

            if dct == {}:
                return True

        return False
