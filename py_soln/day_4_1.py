import numpy as np
import sys

def batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

def is_bingo(card):
    for i in range(5):
        row_zeros=np.count_nonzero(card[i])
        col_zeros=np.count_nonzero(card[:,i])
        if not row_zeros or not col_zeros: #check if we have 0 non-zeros
            return True
    return False

with open('../inputs/day_4_1_input.txt') as f:
    lines = f.readlines()

    nums = lines[0].strip().split(',')
    print(nums)

    boards = []
    board_wins = {}

    i = 0
    for b in batch(lines[1:], 6):
        board = []
        boardIdx = {}
        for l in b[1:]:
            for x in l.strip().split():
                if x == "0":
                    x = "100"
                board.append(int(x))
        boards.append(np.array(board))
        board_wins[i] = False
        i += 1

    #print(boards)
    for n in nums:
        if n == "0":
            n = "100"

        for i, b in enumerate(boards):
            b = np.where(b == int(n), 0, b)
            boards[i] = b
            #print("n: " + n)
            #print(b.reshape(5,5))
            #print(is_bingo(b.reshape(5,5)))
            if is_bingo(b.reshape(5,5)):
                ans_sum = np.sum(np.where(b == 100, 0, b))

                print("SUM: " + str(ans_sum))
                print("NUM: " + n)
                print("Day 4 Answer: " + str(ans_sum*int(n)))
                if i in board_wins:
                    del board_wins[i]
                if len(board_wins) == 0:
                    sys.exit()




