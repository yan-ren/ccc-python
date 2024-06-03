from queue import Queue


t = int(input())

for _ in range(t):
    row = int(input())
    col = int(input())
    # input() -> "+||*+"
    # list("+||*+") -> ['+', '|', '|', '*', '+']
    maze = [list(input()) for _ in range(row)]
    visited = [[False] * col for _ in range(row)]
    step = [[0] * col for _ in range(row)]

    visited[0][0] = True
    step[0][0] = 1

    q = Queue()
    q.put((0, 0))

    while not q.empty():
        r, c = q.get()
        # check if can move up
        if (maze[r][c] == '+' or maze[r][c] == '|') and r > 0 and maze[r - 1][c] != '*' and not visited[r - 1][c]:
            visited[r - 1][c] = True
            step[r - 1][c] = step[r][c] + 1
            q.put((r - 1, c))
        # check if can move down
        if (maze[r][c] == '+' or maze[r][c] == '|') and r < row - 1 and maze[r + 1][c] != '*' and not visited[r + 1][c]:
            visited[r + 1][c] = True
            step[r + 1][c] = step[r][c] + 1
            q.put((r + 1, c))
        # check if can move left
        if (maze[r][c] == '+' or maze[r][c] == '-') and c > 0 and maze[r][c - 1] != '*' and not visited[r][c - 1]:
            visited[r][c - 1] = True
            step[r][c - 1] = step[r][c] + 1
            q.put((r, c - 1))
        # check if can move right
        if (maze[r][c] == '+' or maze[r][c] == '-') and c < col - 1 and maze[r][c + 1] != '*' and not visited[r][c + 1]:
            visited[r][c + 1] = True
            step[r][c+1] = step[r][c] + 1
            q.put((r, c + 1))

    if visited[row - 1][col - 1]:
        print(step[row - 1][col - 1])
    else:
        print(-1)