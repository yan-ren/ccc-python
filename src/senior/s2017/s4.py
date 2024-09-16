'''
This question is based on MST

facts:
- first N-1 edges give a spanning tree, MST also has N-1 edges
- apply D to the largest weight edges in MST, otherwise wasted

notes:
find MST usually involves sorting edges, in this problem, edges may have the same weight
for edge with same weight, put edge in current plan at first, then follow bny the edge not used
Otherwise may use additional unnecessary edge, which in current plan already has same weighted edge

sub problem
- kruskal & disjoint set

in the problem each edge/pipe contains info: two cities, weight, used
'''
class Edge:
    def __init__(self, x, y, weight, used):
        self.x = x
        self.y = y
        self.weight = weight
        self.used = used

    # helper function that for comparison
    def __lt__(self, other):
        if self.weight != other.weight:
            return self.weight < other.weight
        return self.used and not other.used


class DisjoinSets:
    def __init__(self, num_elements):
        self.array = [-1] * num_elements

    # returns the root of the set
    def find(self, x):
        if self.array[x] < 0:
            return x
        self.array[x] = self.find(self.array[x])
        return self.array[x]

    # check if x and y is in the same set
    def is_union(self, x, y):
        return self.find(x) == self.find(y)

    # join two sets that includes x, y
    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)

        if self.array[root2] < self.array[root1]:
            self.array[root1] = root2
        else:
            if self.array[root1] == self.array[root2]:
                self.array[root1] = -1
            self.array[root2] = root1


first_line = input().split()
N = int(first_line[0])
M = int(first_line[1])
D = int(first_line[2])

disjoint_set = DisjoinSets(N+1)
edges = []
# first N-1 edges are the current plan
for _ in range(N-1):
    line = input().split()
    edges.append(Edge(int(line[0]), int(line[1]), int(line[2]), True))

# remaining edges are used edges
for _ in range(M-(N-1)):
    line = input().split()
    edges.append(Edge(int(line[0]), int(line[1]), int(line[2]), False))

# sort edge by customized lt
edges.sort()

max_edge_in_plan = Edge(0, 0, 0, True)
cost_days = 0
used_edges = 0

# Kruskal
for edge in edges:
    if used_edges == N-1:
        break

    if not disjoint_set.is_union(edge.x, edge.y):
        # this edge is added to MST and two vertices are connected
        disjoint_set.union(edge.x, edge.y)
        if not edge.used:
            cost_days += 1
        max_edge_in_plan = edge # since edges are sorted increasing order, later edge is larger edge
        used_edges += 1

disjoint_set = DisjoinSets(N+1)

# recheck with a possible day reduction using reducer D
if not max_edge_in_plan.used:
    # form a new MST. This means loop through all edges in MST
    for edge in edges:
        if not disjoint_set.is_union(edge.x, edge.y):
            if edge.weight < max_edge_in_plan.weight or (edge.weight == max_edge_in_plan.weight and edge.used):
                disjoint_set.union(edge.x, edge.y)
            # if apply D to this edge, this edge makes no cost but can save one day
            # the goal is still trying to find the min cost, the min cost can achieve if D is used to completely reduce
            # the cost of an edge to 0
            elif edge.used and edge.weight <= D:
                cost_days -= 1
                break

