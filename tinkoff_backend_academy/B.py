def main():
    week_1 = input().split()
    week_2 = input().split()
    week_3 = input().split()
    week_4 = input().split()

    days = [True for _ in range(28)] + [False]
    days_ot_week = {"MON": 0, "TUE": 1, "WED": 2, "THU": 3, "FRI": 4, "SAT": 5, "SUN": 6}

    if len(week_1) != 0:
        for dotw in week_1:
            days[days_ot_week[dotw]] = False

    if len(week_2) != 0:
        for dotw in week_2:
            days[7 + days_ot_week[dotw]] = False

    if len(week_3) != 0:
        for dotw in week_3:
            days[14 + days_ot_week[dotw]] = False

    if len(week_4) != 0:
        for dotw in week_4:
            days[21 + days_ot_week[dotw]] = False

    closed = True
    opened = []
    start = 0
    length = 0
    for i in range(29):
        if days[i]:
            length += 1
            if closed:
                start = i
                closed = False
        else:
            if not closed:
                opened.append((length, start))
                length = 0
                closed = True

    opened.sort(key=lambda x: (-x[0], x[1]))

    if opened:
        start = opened[0][1] + 1
        print(start, start + opened[0][0] - 1)
    else:
        print(0, 0)


if __name__ == "__main__":
    main()
