import numpy as np
import sys
from skimage.graph import MCP


R = 100
C = 100

def min_cost(cost, m, n):

    tc = np.zeros((R*5,C*5))
    tc[0][0] = cost[0][0]
    for j in range(1, n+1):
        tc[0][j] = tc[0][j-1] + cost[0][j]
    for i in range(1, m+1):
        tc[i][0] = tc[i-1][0] + cost[i][0]

    #for i in range(1, m+1):
        #for j in range(1, n+1):
            #tc[i][j] = min(tc[i-1][j], tc[i][j-1]) + cost[i][j]

    for i in range(1, m):
        for j in range(1, n):
            tc[i][j] = min(tc[i-1][j], tc[i][j-1], tc[i][j+1], tc[i+1][j]) + cost[i][j]

    print(tc)
    print("=============")
    return tc[m][n]


with open('../inputs/day_15_input.txt') as f:
    lines = f.readlines()

    cost = np.zeros((R,C))
    for i, l in enumerate(lines):
            for j, c in enumerate(list(l.strip())):
                cost[i][j] = int(c)

    cost = np.block([[(cost+i+j-1)%9+1 for i in range(5)]
                             for j in range(5)])
    np.set_printoptions(threshold=sys.maxsize)

    print(np.shape(cost))

    print(int(min_cost(cost, 499,499) - cost[0][0]))

    f = lambda A: MCP(A, fully_connected=0).find_costs([(0,0)])[0]
    #print(f(cost)[0])


