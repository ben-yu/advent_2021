import numpy as np
import sys

simple_digit_counts = {
    2: [1],
    3: [7],
    4: [4],
    7: [8]
}
simple_digit_map = {
    2: 'cf',
    3: 'acf',
    4: 'bcdf',
    7: 'abcdefg'
}

digit_sets = [
    set(list('abcefg')),
    set(list('cf')),
    set(list('acdeg')),
    set(list('acdfg')),
    set(list('bcdf')),
    set(list('abdfg')),
    set(list('abdefg')),
    set(list('acf')),
    set(list('abcdefg')),
    set(list('abcdfg'))
]

with open('../inputs/day_8_input.txt') as f:
    lines = f.readlines()
    count = 0

    for line in lines:
        entry = line.strip().split(' | ')
        inputs = entry[0].split(' ')
        outputs = entry[1].split(' ')

        cur_mapping = {}
        for i in inputs:
            if len(i) in simple_digit_counts:
                cur_mapping[simple_digit_counts[len(i)][0]] = set(list(i))
        # Figure out length 6's
        # Find 9 by diffing 4 and 7
        for i in inputs:
            if len(i) == 6 and len(set(list(i)) - set.union(cur_mapping[4],cur_mapping[7])) == 1:
                cur_mapping[9] = set(list(i))
        # Find 0 by diffing 9 and 7
        for i in inputs:
            if len(i) == 6 and all(s in i for s in cur_mapping[7]) and set(list(i)) != cur_mapping[9]:
                cur_mapping[0] = set(list(i))

        # Find 6 by last remaining len 6
        for i in inputs:
            if len(i) == 6 and set(list(i)) != cur_mapping[0]  and set(list(i)) != cur_mapping[9]:
                cur_mapping[6] = set(list(i))

        # 3 is the only digit that overlaps 7
        for i in inputs:
            if len(i) == 5 and all(s in i for s in cur_mapping[7]):
                cur_mapping[3] = set(list(i))

        # diff 8 and 9 to find position e
        e = min(cur_mapping[8] - cur_mapping[9])

        # 2 is len 5 and has segment e
        for i in inputs:
            if len(i) == 5 and e in i:
                cur_mapping[2] = set(list(i))
        # 5 is last one with len 5
        for i in inputs:
            if len(i) == 5 and set(list(i)) != cur_mapping[3] and set(list(i)) != cur_mapping[2]:
                cur_mapping[5] = set(list(i))

        ordered_sets = []
        for i in range(10):
            ordered_sets.append(cur_mapping[i])

        output_str = ""
        for i in outputs:
            output_str += str(ordered_sets.index(set(list(i))))
        print("OUTPUT {}".format(output_str))
        count += int(output_str)

    print("Day 8 Answer: {}".format(count))






