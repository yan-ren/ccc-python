word = list(input())
rows = int(input())
cols = int(input())

grid = []
count = 0

for i in range(rows):
    grid.append(input().split())


'''
d = index in the word
x, y = current row, col index
dx = x direction
dy = y direction
'''
def search(d, x, y, dx, dy):
    global count
    if x < 0 or x >= rows or y < 0 or y >= cols:
        return
    if word[d] != grid[x][y]:
        return
    if d == len(word) - 1:
        count += 1
        return

    search(d + 1, x+dx, y+dy, dx, dy)
#   just in case need to turn right angle
    if d >= 1:
        search(d + 1, x - dy, y + dx, -dy, dx)
        search(d + 1, x + dy, y - dx, dy, -dx)


for i in range(rows):
    for j in range(cols):
        if word[0] == grid[i][j]:
            search(0, i, j, -1, -1)
            search(0, i, j, -1, 0)
            search(0, i, j, -1, 1)
            search(0, i, j, 0, -1)
            search(0, i, j, 0, 1)
            search(0, i, j, 1, -1)
            search(0, i, j, 1, 0)
            search(0, i, j, 1, 1)


print(count)
