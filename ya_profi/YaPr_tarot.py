"""
There's a list of numbers from 1 to very big, unsorted, numbers can repeat, min len is 1. The task is to determine the
expected value of this random value: take random 4 numbers from the list (they can repeat), then remove the smallest,
then sum them up.
Among several lists, you need to choose one with the highest expected value.
"""

from itertools import combinations_with_replacement
from collections import Counter
import numpy as np


n_decks = int(input())

best_deck = -1
best_mu = -1

for i in range(n_decks):
    _ = int(input())
    cards = list(map(int, input().split()))
    cards_dict = Counter(cards)

    total_denom = 0
    total_sum = 0
    for comb in combinations_with_replacement(set(cards), 4):
        comb_set = set(comb)
        L = len(comb_set)

        factor = 1
        if L == 4:
            factor = np.multiply(factor, 24)
        elif L == 3:
            factor = np.multiply(factor, 12)
        elif L == 2:
            factor = np.multiply(factor, 4) if 1 in Counter(comb).values() else np.multiply(factor, 6)

        factor = np.multiply(factor, np.prod([np.power(cards_dict[key], comb.count(key)) for key in comb_set]))

        total_sum = np.add(total_sum, np.multiply(np.subtract(sum(comb), min(comb)), factor))
        total_denom = np.add(total_denom, factor)

    mu = np.divide(total_sum, total_denom)

    if mu > best_mu:
        best_deck = i + 1
        best_mu = mu

print(best_deck, best_mu)
