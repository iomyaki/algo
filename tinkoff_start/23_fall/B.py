from math import floor


st = input()

if 's' not in st or 'h' not in st or 'e' not in st or 'r' not in st or 'i' not in st or 'f' not in st:
    print(0)
else:
    n_s = st.count('s')
    n_h = st.count('h')
    n_e = st.count('e')
    n_r = st.count('r')
    n_i = st.count('i')
    n_f = floor(st.count('f') / 2)
    print(min(n_s, n_h, n_e, n_r, n_i, n_f))
