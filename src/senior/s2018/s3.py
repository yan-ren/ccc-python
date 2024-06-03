import sys
from collections import deque


class Node:
    def __init__(self, x, y, steps):
        self.x = x
        self.y = y
        self.steps = steps


# Constants
WALL = 'W'
EMPTY = '.'
START = 'S'
CAMERA = 'C'
LEFT = 'L'
RIGHT = 'R'
UP = 'U'
DOWN = 'D'
INF = sys.maxsize

# Read input
input_data = sys.stdin.read().strip().split()
N = int(input_data[0])
M = int(input_data[1])
data = []
start_x = start_y = 0
camera_list = []

# Initialize grid
for i in range(N):
    line = input_data[2 + i]
    row = list(line)
    data.append(row)
    for j, cell in enumerate(row):
        if cell == START:
            start_x, start_y = i, j
        if cell == CAMERA:
            camera_list.append(Node(i, j, -1))

# Initialize route and visited arrays
route = [[INF] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]


def update_route(x, y):
    if data[x][y] == WALL:
        return False
    if data[x][y] in {EMPTY, START}:
        route[x][y] = -1
    return True


def handle_cameras():
    for camera in camera_list:
        x, y = camera.x, camera.y
        route[x][y] = -1
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x, y
            while 0 <= nx < N and 0 <= ny < M:
                if not update_route(nx, ny):
                    break
                nx += dx
                ny += dy


def process_node(node, x, y):
    if route[x][y] == -1:
        return False
    if data[x][y] == EMPTY:
        if visited[x][y] and route[x][y] <= node.steps + 1:
            return False
        route[x][y] = node.steps + 1
    elif data[x][y] in {LEFT, DOWN, RIGHT, UP}:
        if visited[x][y] and route[x][y] <= node.steps:
            return False
        route[x][y] = node.steps
    else:
        return False
    return True


def enqueue_node(queue, node, x, y):
    if process_node(node, x, y):
        visited[x][y] = True
        queue.append(Node(x, y, route[x][y]))


# Handle cameras
handle_cameras()

# BFS initialization
queue = deque()
if route[start_x][start_y] != -1:
    route[start_x][start_y] = 0
    visited[start_x][start_y] = True
    queue.append(Node(start_x, start_y, 0))

# BFS loop
while queue:
    current = queue.popleft()
    cx, cy = current.x, current.y
    directions = []
    if data[cx][cy] == LEFT:
        directions.append((cx, cy - 1))
    elif data[cx][cy] == RIGHT:
        directions.append((cx, cy + 1))
    elif data[cx][cy] == UP:
        directions.append((cx - 1, cy))
    elif data[cx][cy] == DOWN:
        directions.append((cx + 1, cy))
    elif data[cx][cy] in {EMPTY, START}:
        directions.extend([(cx, cy - 1), (cx, cy + 1), (cx - 1, cy), (cx + 1, cy)])

    for nx, ny in directions:
        if 0 <= nx < N and 0 <= ny < M:
            enqueue_node(queue, current, nx, ny)

# Output results
for i in range(N):
    for j in range(M):
        if data[i][j] == EMPTY:
            result = route[i][j]
            if result == INF:
                result = -1
            print(result)
