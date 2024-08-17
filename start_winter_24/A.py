n = int(input())

for i in range(n):
    letters = input()
    if {letter: letters.count(letter) for letter in set(letters)} == {'T': 1, 'I': 1, 'N': 1, 'K': 1, 'O': 1, 'F': 2}:
        print('Yes')
    else:
        print('No')
