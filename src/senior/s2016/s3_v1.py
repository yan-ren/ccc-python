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
def dfs(start):
    max_depth = 0
    farthest_node = start
    visited = set()
    stack = [(start, 0)]

    while stack:
        node, depth = stack.pop()
        visited.add(node)

        if depth > max_depth:
            max_depth = depth
            farthest_node = node

        for neighbor in tree[node]:
            if neighbor not in visited:
                stack.append((neighbor, depth + 1))

    return farthest_node, max_depth


# Step 1: Choose any random Pho restaurant as the starting point
start = next(iter(pho_restaurants))
# Step 2: Find the farthest Pho restaurant from the chosen starting point
farthest_pho, _ = dfs(start)
# Step 3: Perform DFS from the farthest Pho restaurant to find the longest path
_, longest_path = dfs(farthest_pho)

total_edges = sum(len(neighbors) for neighbors in tree.values()) // 2

min_travel_time = total_edges * 2 - longest_path
print(min_travel_time)

