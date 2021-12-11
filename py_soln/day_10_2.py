
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

complete_brace_points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
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

def score_line(l, score):
    char_stack = []
    for c in list(l.strip()):
        if c in brace_match:
            if char_stack[-1] != brace_match[c]:
#                print("{} -> Expected {} but found {}".format(l, reverse_brace_match[char_stack[-1]], c))
                return brace_points[c]
            char_stack.pop()
        else:
            char_stack.append(c)
    char_stack.reverse()
    a = list(map(lambda x: reverse_brace_match[x], char_stack))
    for c in a:
        score = (score * 5) + complete_brace_points[c]
    return score

with open('../inputs/day_10_input.txt') as f:
    lines = f.readlines()

    points = 0
    incomplete_lines = []
    for l in lines:
        if check_line(l) == 0:
            incomplete_lines.append(l)

    scores = []
    for l in incomplete_lines:
        score = 0
        score = score_line(l, score)
        scores.append(score)
        print(score)

    scores.sort()

    print("Answer {}".format(scores[int(len(scores)/2)]))

