
from collections import defaultdict

def print_paths_util(graph, start, end, visited, double_visit, paths, path):

    if start.islower() and visited[start] < 1:
        visited[start] += 1
    elif start.islower() and visited[start] < 2 and double_visit is None:
        visited[start] += 1
        double_visit = start
    path.append(start)

    if start == end:
        paths.append(path)
        print(path)
    else:
        for i in graph[start]:
            if visited[i] < 1 or (visited[i] < 2 and double_visit == None and i != 'start' and i != 'end'):
                print_paths_util(graph, i,end,visited, double_visit, paths, path)

    path.pop()
    visited[start] -= 1
    if start == double_visit:
        double_visit = None

def print_paths(graph, start, end):
    visited = defaultdict(int)
    double_visit = None
    paths = []
    path = []

    print_paths_util(graph, start, end, visited, double_visit, paths, path)
    return paths




with open('../inputs/day_12_input.txt') as f:
    lines = f.readlines()

    graph = defaultdict(list)

    for l in lines:
        res = l.strip().split('-')
        graph[res[0]].append(res[1])
        graph[res[1]].append(res[0])


    paths = print_paths(graph, 'start', 'end')
    print("Answer {}".format(len(paths)))

