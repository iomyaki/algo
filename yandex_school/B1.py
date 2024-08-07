a, b = input(), input()

b_list, b_list_minus = [], []
command = ''
command_active = False
for s in b:
    if s == '<':
        command_active = True
    elif s == '>':
        command_active = False

        if command == 'delete':
            if len(b_list_minus) != 0:
                b_list_minus.pop()
        elif command == 'bspace':
            if len(b_list) != 0:
                b_list.pop()
        elif command == 'left':
            if len(b_list) != 0:
                b_list_minus.append(b_list.pop())
        elif command == 'right':
            if len(b_list_minus) != 0:
                b_list.append(b_list_minus.pop())

        command = ''

    else:
        if command_active:
            command += s
        else:
            b_list.append(s)


b_list += b_list_minus[::-1]  # this line is absent in a solution that has been sent

if b_list == list(a):
    print('Yes')
else:
    print('No')

# WA test 17
