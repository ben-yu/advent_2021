import numpy as np
import sys
import collections as cl



def check_adj(heights, i, j):
    lowest = True

    if i > 0 and heights[j][i-1] <= heights[j][i]:
        lowest = False
    if j > 0 and heights[j-1][i] <= heights[j][i]:
        lowest = False
    if i < len(heights[j])-1 and heights[j][i+1] <= heights[j][i]:
        lowest = False
    if j < len(heights)-1 and heights[j+1][i] <= heights[j][i]:
        lowest = False

    return lowest

with open('../inputs/day_9_input.txt') as f:
    lines = f.readlines()

    heights = []
    for l in lines:
        heights.append(list(map(lambda x: int(x), list(l.strip()))))

    print(len(heights))

    risk = 0
    for j  in range(len(heights)):
        for i in range(len(heights[j])):
            if check_adj(heights, i, j):
                print(heights[j][i]+1)
                risk += heights[j][i] + 1

    print("Risk {}".format(risk))

