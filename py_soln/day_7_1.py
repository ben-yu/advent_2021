import numpy as np
import sys

@lru_cache(maxsize=10000)
def arithmetic_sum(n):
    return sum(i for i in range(1, n+1))

with open('../inputs/day_7_input.txt') as f:
    lines = f.readlines()
    inputs = lines[0].strip().split(',')

    nums = [int(x) for x in inputs]

    lower_bound = min(nums)
    upper_bound = max(nums)

    min_sum = sys.maxsize
    for i in range(lower_bound, upper_bound+1):
        #part 1: cost = sum(map(lambda x: abs(x-i), nums))
        cost = sum(map(lambda x: arithmetic_sum(abs(x-i)), nums))
        if cost <  min_sum:
            min_sum = cost
            best_dist = i

    print(min_sum)


