import numpy as np
import sys
from collections import deque as queue
dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]

def isValid(vis, grid, row, col):
    if row < 0 or col < 0 or row >= len(vis) or col >= len(vis[0]):
        return False
    if grid[row][col] == 9:
        return False
    if vis[row][col]:
        return False
    return True

def BFS(grid, vis, row, col):
    q = queue()
    q.append(( row, col ))
    vis[row][col] = 1

    # Iterate while the queue
    # is not empty
    while (len(q) > 0):
        x,y = q.popleft()

        # Go to the adjacent cells
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if (isValid(vis, grid, adjx, adjy)):
                print(adjx, adjy)
                q.append((adjx, adjy))
                vis[adjx][adjy] = 1

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

    low_points = []
    for j  in range(len(heights)):
        for i in range(len(heights[j])):
            if check_adj(heights, i, j):
                low_points.append((j,i))

    areas = []
    for j, i in low_points:
        vis = []
        for x in range(len(heights)):
            a = []
            for y in range(len(heights[0])):
                a.append(0)
            vis.append(a)
        #print(vis)

        BFS(heights, vis, j, i)
        area = np.sum(vis)
        areas.append(area)
        print(vis)
        print("{} -> {}".format((j,i), area))

    areas.sort(reverse=True)

    print("Answer {}".format(areas[0]*areas[1]*areas[2]))

