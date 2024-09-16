import sys
from collections import defaultdict, deque
sys.setrecursionlimit(1000000)

data = input().split()
# Number of restaurants and number of Pho restaurants
N = int(data[0])
M = int(data[1])

# Pho restaurants
pho_restaurants = set()
data = input().split()
# Any pho restaurant can be the starting point
start = int(data[0])
for pho in data:
    pho_restaurants.add(int(pho))

# Adjacency list for the tree
tree = defaultdict(list)
for _ in range(N - 1):
    data = input().split()
    a = int(data[0])
    b = int(data[1])
    tree[a].append(b)
    tree[b].append(a)

# Step 4: Prune the tree to remove non-Pho leaves
def prune_tree(tree, pho_restaurants):
    visited = [False] * N
    leaves = deque()
    for node in range(N):
        if node not in pho_restaurants and len(tree[node]) == 1:
            leaves.append(node)

    while leaves:
        leaf = leaves.popleft()
        visited[leaf] = True
        for neighbor in tree[leaf]:
            if not visited[neighbor]:
                # remove useless leaf from the tree
                tree[neighbor].remove(leaf)
                # if the parent of the leaf is still useless, remove it as well
                if len(tree[neighbor]) == 1 and neighbor not in pho_restaurants:
                    leaves.append(neighbor)


prune_tree(tree, pho_restaurants)

# Step 5: Calculate the minimum travel time using DFS
max_diameter = 0
def dfs(node, parent):
    global max_diameter

    max_depth = 0
    second_max_depth = 0
    total_edges = 0

    for neighbor in tree[node]:
        if neighbor != parent:
            depth, edges = dfs(neighbor, node)
            total_edges += edges
            if depth > max_depth:
                second_max_depth = max_depth
                max_depth = depth
            elif depth > second_max_depth:
                second_max_depth = depth

    max_diameter = max(max_diameter, max_depth + second_max_depth)
    return max_depth + 1, total_edges + 1


_, total_edges = dfs(start, -1)

# The answer is total_edges - 1 - max_diameter
print((total_edges - 1) * 2 - max_diameter)

