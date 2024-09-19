try:
    s = input()
    words = s.split()

    phrases = {}
    for i in range(0, len(words) - 1):
        phrase = f"{words[i]} {words[i + 1]}"
        phrases[phrase] = phrases.get(phrase, 0) + 1

    counts = sorted(phrases.items(), key=lambda x: x[1])
    for count in counts:
        if count[1] > 1:
            print(f"{count[0]}: {count[1]}")
except EOFError:
    pass
