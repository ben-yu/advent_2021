import numpy as np
import sys
import collections as cl


with open('../inputs/day_5_1_input.txt') as f:
    lines = f.readlines()

    MAX = 1000
    q2 = True

    grid = np.zeros((MAX,MAX))
    for l in lines:
        res = l.split(' -> ')
        a = res[0].strip().split(',')
        b = res[1].strip().split(',')

        a0 = int(a[0])
        a1 = int(a[1])
        b0 = int(b[0])
        b1 = int(b[1])

        if a0 == b0: # vertical
            y1, y2 = min(a1, b1), max(a1, b1)
            grid[y1:y2+1, a0] += 1

        elif a1 == b1: # horizontal
            x1, x2 = min(a0, b0), max(a0, b0)
            grid[a1, x1:x2+1] += 1

        elif abs(b1-a1) == abs(b0-a0) and q2: # diagonal
            if a0 < b0:
                x_range = range(a0, b0+1)
            else:
                x_range = range(a0, b0-1, -1)

            if a1 < b1:
                y_range = range(a1, b1+1)
            else:
                y_range = range(a1, b1-1, -1)

            for x, y in zip(x_range, y_range):
                grid[y,x] += 1

    print(grid)
    print("Day 5 Answer: {}".format(np.sum(np.where(grid > 1, 1, 0))))
