import numpy as np
import sys
import collections as cl


brace_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

brace_match = {
    '}': '{',
    ']': '[',
    ')': '(',
    '>': '<'
}
reverse_brace_match = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>'
}

def check_line(l):

    char_stack = []
    for c in list(l.strip()):
        if c in brace_match:
            if char_stack[-1] != brace_match[c]:
#                print("{} -> Expected {} but found {}".format(l, reverse_brace_match[char_stack[-1]], c))
                return brace_points[c]
            char_stack.pop()
        else:
            char_stack.append(c)
    return 0

with open('../inputs/day_10_input.txt') as f:
    lines = f.readlines()

    points = 0
    for l in lines:
        points += check_line(l)

    print("Points {}".format(points))

