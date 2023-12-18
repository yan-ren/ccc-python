N = int(input())

graph = {}

visited = [False for i in range(N+1)]

min_distance = N + 1
distance = [min_distance for i in range(N+1)]

for i in range(1, N+1):
    line = input().split()
    if int(line[0]) == 0:
        graph[i] = []
        continue

    neighbors = []
    for j in range(1, len(line)):
        neighbors.append(int(line[j]))
    graph[i] = neighbors


stack = [1]
visited[1] = True
distance[1] = 1

while len(stack) > 0:
    current_node = stack.pop()
    current_distance = distance[current_node]

    # if current node is end node, cannot go anywhere
    if len(graph[current_node]) == 0:
        if min_distance > current_distance:
            min_distance = current_distance

    for neighbor in graph[current_node]:
        if current_distance+1 < distance[neighbor]:
            distance[neighbor] = current_distance + 1
            visited[neighbor] = False
        if visited[neighbor] == 0:
            stack.append(neighbor)
            visited[neighbor] = True

all_visited = True
for i in range(1, len(visited)):
    if not visited[i]:
        all_visited = False

if all_visited:
    print("Y")
else:
    print("N")

print(min_distance)
