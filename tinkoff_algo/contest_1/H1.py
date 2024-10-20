_ = input()
st = input()

#st = 'AAB'
st = ''.join(sorted(st))

st_dict = {i: 0 for i in st}

for letter in st:
    st_dict[letter] += 1

answer = ''
single_letter = ''
single_letter_needed = True
for letter in st_dict.keys():
    if single_letter_needed and st_dict[letter] % 2 != 0:
        single_letter_needed = False
        single_letter = letter
    if st_dict[letter] >= 2:
        answer += letter * (st_dict[letter] // 2)

answer = answer + single_letter + answer[::-1]

print(answer)
