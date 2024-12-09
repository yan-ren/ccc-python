'''
Observation:
1. No matter how stations swap, the walkways do not change
2. To travel from station 1 to N, there are two valid path, it's either travel by train only
or start with train then walk to station N if there is walkway
because if we start travel by walking and we end up at station that is ahead of train, we
can only continue with walking since train is behind, we need to wait to get on the train
so, walk + train is not valid combination
This mean we can only get off from the train once, because go back to the train requires
the train is at the same station as our current station, waiting for train to arrive is equivalent
to taking the train to that station

solution
1. simulate to graph problem, turn this problem into single source shortest path problem
This gives 7/15, due to runtime

2. full mark
- first, calculate the distance from evey node to the end if we only travel by walking, if walkway exists
  walk_distance - BFS in reverse order, meaning start from end station
- second, calculate the train+walk option, find the min (position i in the routes + walk_distance[i])
'''
from collections import defaultdict, deque
import heapq

'''
BFS from station N to all other stations only by walkway
'''
def bfs(end_station, walkways, walk_distance):
    visited = set()
    queue = deque([end_station])
    visited.add(end_station)

    walk_distance[end_station - 1] = 0

    while queue:
        current = queue.popleft()
        for neighbor in walkways[current]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            walk_distance[neighbor-1] = walk_distance[current-1] + 1
            queue.append(neighbor)


N, W, D = map(int, input().split())
walkways = defaultdict(list) # each value is empty list by default
# key is the node, value is the list of node that can reach from the key node

for _ in range(W):
    a, b = map(int, input().split())
    walkways[b].append(a) # we store walkway in reverse order because bfs starts from the end

walk_distance = [-1 for _ in range(N)] # walk_distance[i-1] represents the walk from station i to end station

# bfs from the end station to populate the walk_distance
bfs(N, walkways, walk_distance)

stations = list(map(int, input().split()))
# consider using heap to maintain the travel cost of train + walk
# then take each station swap into consider
# another useful data structure for this is called multiset

heap = []
for i in range(N):
    # if there is no way to walk from station i to station N, don't consider train+walk option
    if walk_distance[stations[i] - 1] == -1:
        continue
    # i: travel time by train + walk time from station i to station N
    heapq.heappush(heap, (i + walk_distance[stations[i] - 1], i)) # use travel time as priority,
                                                                        # station number is the second value

# now consider the station swapping
for _ in range(D):
    x, y = map(int, input().split())
    stations[x-1], stations[y-1] = stations[y-1], stations[x-1]
    # station swaps makes new train time from station 1 to x,y
    if walk_distance[stations[x-1] - 1] != -1:
        heapq.heappush(heap, (x - 1 + walk_distance[stations[x-1] - 1], x - 1))
    if walk_distance[stations[y-1] - 1] != -1:
        heapq.heappush(heap, (y - 1 + walk_distance[stations[y-1] - 1], y - 1))

    # (y - 1 + walk_distance[stations[y - 1] - 1], y - 1)
    # careful, at this step, we only put the new travel time, but do not remove the old travel time
    # min_travel = train to station + walk distance from that station to station N, recalculate to reflect the current station order
    min_travel = heap[0][1] + walk_distance[stations[heap[0][1]] - 1]
    # pop out all invalid travel time caused by swapping, if recalculate value doesn't match with value stored in the heap
    # meaning the value in the heap is outdated
    while min_travel != heap[0][0]:
        heapq.heappop(heap)
        min_travel = heap[0][1] + walk_distance[stations[heap[0][1]] - 1]
    print(heap[0][0])
