import copy
from collections import Counter
import functools

rules = {}
@functools.lru_cache
def count_figures(pair, step):
    if step == 40:
        return Counter(list(pair))

    insert = rules[pair]

    c = Counter()
    c += count_figures(pair[0] + insert, step+1)
    c += count_figures(insert+pair[1], step+1)
    c[insert] -= 1
    return c

with open('../inputs/day_14_input.txt') as f:
    lines = f.readlines()

    base = lines[0].strip()

    for l in lines:
        if '->' in l:
            res = l.strip().split(' -> ')
            rules[res[0]] = res[1]

    counts = Counter()
    for j in range(len(base)-1):
        counts[f'{base[j]}{base[j+1]}'] += 1

    steps = 40
    for i in range(steps):
        new_counts = counts.copy()
        for k, v in counts.items():
            if v > 0:
                insert = rules[k]
                new_counts[f'{k[0]}{insert}'] += v
                new_counts[f'{insert}{k[1]}'] += v
                new_counts[k] -= v
        counts = new_counts

    letter_count = Counter()
    for k, v in counts.items():
        for c in k:
            letter_count[c] += v

    letter_count[base[0]] += 1
    letter_count[base[-1]] += 1

    for key in letter_count.keys():
        letter_count[key] //= 2

    res = letter_count.most_common()
    print(res[0], res[-1], res[0][1]-res[-1][1])





