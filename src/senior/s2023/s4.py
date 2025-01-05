import heapq


# Define a function to calculate the shortest distance between two nodes
def distance(start, end):
    pq = [(0, start)]  # Priority queue, stores (distance, node)
    distances = [float('inf')] * (n_nodes + 1)  # Distance array, initialized to infinity
    distances[start] = 0  # Distance from the start node to itself is 0
    while pq:
        dist, node = heapq.heappop(pq)
        if node == end:
            return dist
        for adj, adj_dist, _, i in graph[node]:
            if i in cannot_use:
                continue
            new_dist = dist + adj_dist
            if distances[adj] > new_dist:
                heapq.heappush(pq, (new_dist, adj))
                distances[adj] = new_dist
    return float('inf')  # Return infinity if no path exists


# Read the number of nodes and edges
n_nodes, n_edges = map(int, input().split())
edges = []  # Store all edge information
graph = [[] for _ in range(n_nodes + 1)]  # Adjacency list
cannot_use = set()  # Set of edges that cannot be used
# Read edge information and construct the graph
for i in range(n_edges):
    a, b, dist, cost = map(int, input().split())
    edges.append((a, b, dist, cost, i))
    graph[a].append((b, dist, cost, i))
    graph[b].append((a, dist, cost, i))
# Sort edges by cost in descending order
edges.sort(key=lambda x: x[3], reverse=True)
total_cost = 0
for a, b, dist, c, id in edges:
    cannot_use.add(id)
    if distance(a, b) > dist:  # Check if removing the edge affects the shortest path
        cannot_use.remove(id)
        total_cost += c

print(total_cost)
