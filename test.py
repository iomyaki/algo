at = (
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
    (1, 1, 0, 0),
    (1, 0, 1, 0),
    (1, 0, 0, 1),
    (0, 1, 1, 0),
    (0, 1, 0, 1),
    (0, 0, 1, 1),
    (1, 1, 1, 0),
    (1, 1, 0, 1),
    (1, 0, 1, 1),
    (0, 1, 1, 1),
    (1, 1, 1, 1)
)

variants = []
for a in range(15):
    for b in range(15):
        for c in range(15):
            for d in range(15):
                for e in range(15):
                    for f in range(15):
                        variants.append((at[a], at[b], at[c], at[d], at[e], at[f]))

counter = 0
for var in variants:
    if (var[0][0] == 0 and var[1][0] == 0 and var[2][0] == 0 and var[3][0] == 0 and var[4][0] == 0 and var[5][0] == 0) or (var[0][1] == 0 and var[1][1] == 0 and var[2][1] == 0 and var[3][1] == 0 and var[4][1] == 0 and var[5][1] == 0) or (var[0][2] == 0 and var[1][2] == 0 and var[2][2] == 0 and var[3][2] == 0 and var[4][2] == 0 and var[5][2] == 0) or (var[0][3] == 0 and var[1][3] == 0 and var[2][3] == 0 and var[3][3] == 0 and var[4][3] == 0 and var[5][3] == 0):
        counter += 1

print(counter == 4 * 7 ** 6 - 6 * 3 ** 6 - 4)
