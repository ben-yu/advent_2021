import copy
from collections import Counter

with open('../inputs/day_14_input.txt') as f:
    lines = f.readlines()

    base = list(lines[0].strip())
    rules = {}

    for l in lines:
        if '->' in l:
            res = l.strip().split(' -> ')
            rules[res[0]] = res[1]

    steps = 40
    for i in range(steps):
        base_copy = []
        for j in range(len(base)-1):
            base_copy.append(base[j])
            if base[j] + base[j+1] in rules:
                base_copy.append(rules[base[j]+base[j+1]])
        base_copy.append(base[len(base)-1])

        base = base_copy
        #print("After step {}: {}".format(i, base))

    c = Counter(base).most_common()
    print(c[0], c[-1], c[0][1]-c[-1][1])





