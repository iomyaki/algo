has_lower, has_upper, has_digit = False, False, False

counter = 0
for s in input():
    counter += 1

    if has_lower and has_upper and has_digit:
        continue
    elif not has_lower and s.islower():
        has_lower = True
    elif not has_upper and s.isupper():
        has_upper = True
    elif not has_digit and s.isdigit():
        has_digit = True

if counter >= 8 and has_lower and has_upper and has_digit:
    print('YES')
else:
    print('NO')
