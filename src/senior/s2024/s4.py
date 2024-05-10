'''
Minimum Spanning Tree problem in an undirected unweighted graph
original MST, we have undirected weighted graph, find a tree such that contains all vertices and minimizes the sum of
cost of edges

For the unweighted graph, we can find MST using simple approach by DFS or BFS
we need to track the edges when we expanding the tree, assign alternate colors
-> run DFS in unweighted graph and track the edges p
'''
import sys
sys.setrecursionlimit(300000)

line = input().split()
N = int(line[0])
M = int(line[1])

graph = [[] for i in range(N+1)]

for e in range(M):
    line = input().split()
    u = int(line[0])
    v = int(line[1])
    graph[u].append((v, e))
    graph[v].append((u, e))


visited = set()
color_result = ['G'] * M
def dfs(current_node, color):
    for neighbor, edge in graph[current_node]:
        if neighbor not in visited:
            visited.add(neighbor)
            color_result[edge] = color

            if color == 'R':
                new_color = 'B'
            else:
                new_color = 'R'

            dfs(neighbor, new_color)


for vertex in range(1, N+1):
    if vertex not in visited:
        visited.add(vertex)
        dfs(vertex, 'R')


print("".join(color_result))