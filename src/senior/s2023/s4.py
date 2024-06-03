import heapq


# 定义一个函数来计算两个节点之间的最短距离
def distance(start, end):
    pq = [(0, start)]  # 优先队列，存储(距离, 节点)
    distances = [float('inf')] * (n_nodes + 1)  # 距离数组，初始值为无穷大
    distances[start] = 0  # 起点到自身的距离为0
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
    return float('inf')  # 如果没有路径则返回无穷大


# 读取节点数和边数
n_nodes, n_edges = map(int, input().split())
edges = []  # 存储所有边的信息
graph = [[] for _ in range(n_nodes + 1)]  # 邻接表
cannot_use = set()  # 存储不能使用的边的集合
# 读取边的信息并构建图
for i in range(n_edges):
    a, b, dist, cost = map(int, input().split())
    edges.append((a, b, dist, cost, i))
    graph[a].append((b, dist, cost, i))
    graph[b].append((a, dist, cost, i))
# 按成本 从大到小排序 边
edges.sort(key=lambda x: x[3], reverse=True)
total_cost = 0
for a, b, dist, c, id in edges:
    cannot_use.add(id)
    if distance(a, b) > dist:  # 检查移除边后是否影响最短路径
        cannot_use.remove(id)
    total_cost += c
print(total_cost)
