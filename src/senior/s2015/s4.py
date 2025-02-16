"""
CCC 2015 Senior 4: Convex Hull

Problem Description:
Given N islands, M routes between them, and a ship with an initial hull strength K,
we want to find the minimum time required to travel from a start island to an end island.
Each route has a travel time and hull wear factor. The ship can only take a route
if its remaining hull strength is greater than the wear factor. If the ship cannot
reach the target island with the given constraints, the result should be -1.

Algorithmic Approach:
We use a modified Dijkstra's algorithm to find the shortest travel time while also tracking
the remaining hull strength as part of the state. The distance array stores the minimum time
to reach each island with a specific hull strength remaining. We use a priority queue (min-heap)
to efficiently process states in ascending order of travel time.

Key Steps:
1. Initialize distances for each island and hull strength state to infinity.
2. Start with the initial island and full hull strength.
3. For each state popped from the queue, if it's the target island, return the current time.
4. Otherwise, explore all possible routes to neighboring islands, updating distances if
   the hull strength and travel time conditions are met.
5. If no valid path is found, return -1.

Time Complexity:
The algorithm runs in O(M * K) due to the extended state space with hull strength tracking.

Edge Cases to Consider:
- No valid path exists.
- Routes with zero travel time but significant hull wear.
- Routes with high travel time but negligible hull wear.
"""

import heapq


def find_min_travel_time(K, N, M, routes, start, end):
    # Construct graph as adjacency list
    graph = [{} for _ in range(N)]
    for a, b, t, h in routes:
        graph[a - 1].setdefault(b - 1, []).append((t, h))
        graph[b - 1].setdefault(a - 1, []).append((t, h))

    INF = float('inf')
    distance = [[INF] * (K + 1) for _ in range(N)]
    distance[start - 1][K] = 0

    # Min-heap for Dijkstra: (time, island, hull_left)
    queue = [(0, start - 1, K)]
    visited = set()

    while queue:
        time, island, hull_left = heapq.heappop(queue)

        # Stop if we reached the destination
        if island == end - 1:
            return time

        if (island, hull_left) in visited:
            continue

        visited.add((island, hull_left))

        # Explore neighbors
        for neighbor, paths in graph[island].items():
            for travel_time, hull_wear in paths:
                new_hull = hull_left - hull_wear
                new_time = time + travel_time

                if new_hull > 0 and new_time < distance[neighbor][new_hull]:
                    distance[neighbor][new_hull] = new_time
                    heapq.heappush(queue, (new_time, neighbor, new_hull))

    return -1


K, N, M = map(int, input().split())

routes = []

for m in range(M):
    a, b, t, h = map(int, input().split())
    routes.append((a, b, t, h))

start, end = map(int, input().split())

result = find_min_travel_time(K, N, M, routes, start, end)
print(result)
