
from collections import defaultdict

def print_paths_util(graph, start, end, visited, paths, path):

    if start.islower():
        visited[start] = True
    path.append(start)

    if start == end:
        paths.append(path)
        print(path)
    else:
        for i in graph[start]:
            if visited[i] == False:
                print_paths_util(graph, i,end,visited, paths, path)

    path.pop()
    visited[start] = False

def print_paths(graph, start, end):
    visited = defaultdict(bool)
    paths = []
    path = []

    print_paths_util(graph, start, end, visited, paths, path)
    return paths




with open('../inputs/day_12_test.txt') as f:
    lines = f.readlines()

    graph = defaultdict(list)

    for l in lines:
        res = l.strip().split('-')
        graph[res[0]].append(res[1])
        graph[res[1]].append(res[0])


    paths = print_paths(graph, 'start', 'end')
    print("Answer {}".format(len(paths)))
