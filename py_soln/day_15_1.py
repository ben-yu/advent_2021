
R = 100
C = 100

def minCost(cost, m, n):

    tc = [[0 for x in range(C)] for x in range(R)]
    tc[0][0] = cost[0][0]
    for i in range(1, m+1):
        tc[i][0] = tc[i-1][0] + cost[i][0]
    for j in range(1, n+1):
        tc[0][j] = tc[0][j-1] + cost[0][j]

    for i in range(1, m+1):
        for j in range(1, n+1):
            tc[i][j] = min(tc[i-1][j], tc[i][j-1]) + cost[i][j]

    return tc[m][n]


with open('../inputs/day_15_input.txt') as f:
    lines = f.readlines()

    cost = []
    for l in lines:
        row = []
        for c in list(l.strip()):
            row.append(int(c))
        cost.append(row)

    print(minCost(cost, 99,99) - cost[0][0])

