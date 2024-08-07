def main():
    _ = input()
    s = input()

    alphabet = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0,
        'F': 0,
        'G': 0,
        'H': 0,
        'I': 0,
        'J': 0,
        'K': 0,
        'L': 0,
        'M': 0,
        'N': 0,
        'O': 0,
        'P': 0,
        'Q': 0,
        'R': 0,
        'S': 0,
        'T': 0,
        'U': 0,
        'V': 0,
        'W': 0,
        'X': 0,
        'Y': 0,
        'Z': 0
    }

    for c in s:
        alphabet[c] += 1

    first_half, singleton = '', ''

    for letter in alphabet.keys():
        if not singleton and alphabet[letter] % 2 != 0:
            singleton = letter
        if alphabet[letter] >= 2:
            first_half += letter * (alphabet[letter] // 2)

    print(first_half + singleton + first_half[::-1])


if __name__ == '__main__':
    main()
