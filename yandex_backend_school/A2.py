n = int(input())

turns_first = set()
turns_second = set()
first_won = False
second_won = False

for i in range(n):
    if first_won or second_won:
        break
    else:
        current_turn = i

    if i % 2 == 0:
        turns_first.add(tuple(map(int, input().split())))
    else:
        turns_second.add(tuple(map(int, input().split())))

    if i >= 8:
        if i % 2 == 0:
            for turn in turns_first:
                if first_won:
                    break

                for shift in range(5):
                    if first_won:
                        break

                    counter = 0
                    for pos in ((-4, -4), (-3, -3), (-2, -2), (-1, -1), (0, 0)):
                        if (turn[0] + pos[0] + shift, turn[1] + pos[1] + shift) in turns_first:
                            counter += 1
                        else:
                            counter = 0
                            continue
                    if counter == 5:
                        first_won = True
                        break

                    counter = 0
                    for pos in ((-4, 4), (-3, 3), (-2, 2), (-1, 1), (0, 0)):
                        if (turn[0] + pos[0] + shift, turn[1] + pos[1] - shift) in turns_first:
                            counter += 1
                        else:
                            counter = 0
                            continue
                    if counter == 5:
                        first_won = True
                        break

                    counter = 0
                    for pos in (-4, -3, -2, -1, 0):
                        if (turn[0] + pos + shift, turn[1]) in turns_first:
                            counter += 1
                        else:
                            counter = 0
                            continue
                    if counter == 5:
                        first_won = True
                        break

                    counter = 0
                    for pos in (-4, -3, -2, -1, 0):
                        if (turn[0], turn[1] + pos + shift) in turns_first:
                            counter += 1
                        else:
                            counter = 0
                            continue
                    if counter == 5:
                        first_won = True
                        break
        else:
            for turn in turns_second:
                if second_won:
                    break

                for shift in range(5):
                    if second_won:
                        break

                    counter = 0
                    for pos in ((-4, -4), (-3, -3), (-2, -2), (-1, -1), (0, 0)):
                        if (turn[0] + pos[0] + shift, turn[1] + pos[1] + shift) in turns_second:
                            counter += 1
                        else:
                            counter = 0
                            continue
                    if counter == 5:
                        second_won = True
                        break

                    counter = 0
                    for pos in ((-4, 4), (-3, 3), (-2, 2), (-1, 1), (0, 0)):
                        if (turn[0] + pos[0] + shift, turn[1] + pos[1] - shift) in turns_second:
                            counter += 1
                        else:
                            counter = 0
                            continue
                    if counter == 5:
                        second_won = True
                        break

                    counter = 0
                    for pos in (-4, -3, -2, -1, 0):
                        if (turn[0] + pos + shift, turn[1]) in turns_second:
                            counter += 1
                        else:
                            counter = 0
                            continue
                    if counter == 5:
                        second_won = True
                        break

                    counter = 0
                    for pos in (-4, -3, -2, -1, 0):
                        if (turn[0], turn[1] + pos + shift) in turns_second:
                            counter += 1
                        else:
                            counter = 0
                            continue
                    if counter == 5:
                        second_won = True
                        break

if second_won and current_turn < n - 1 or first_won and current_turn < n - 1:
    print('Inattention')
elif first_won:
    print('First')
elif second_won:
    print('Second')
else:
    print('Draw')

# TL test 50
