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

digit_counts = {
    2: [1],
    3: [7],
    4: [4],
    5: [2,3,5],
    6: [0,6,9],
    7: [8]
}

with open('../inputs/day_8_input.txt') as f:
    lines = f.readlines()
    count = 0

    for line in lines:
        entry = line.strip().split(' | ')
        #print(entry)
        inputs = entry[0].split(' ')
        outputs = entry[1].split(' ')

        cur_mapping = {}

        # find simple ones first
        for i in outputs:
            if len(i) in simple_digit_counts:
                count += 1
    print(count)

#        for i in inputs:
#            if len(i) in simple_digit_counts:
#                map_chars = simple_digit_map[len(i)]
#               for a,b in zip(i.split(),map_chars.split()):
#                    cur_mapping[a] = b





