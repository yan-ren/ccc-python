R, C = map(int, input().split())

# initialize 2d list with size (R+1) x (C+1)
lab = [[0] * (C + 1) for _ in range(R + 1)]

k = int(input())
cages = set()
for _ in range(k):
    r, c = map(int, input().split())
    cages.add((r, c))

cages.add((1, 1))
lab[1][1] = 1
for row in range(1, len(lab)):
    for col in range(1, len(lab[row])):
        if (row, col) not in cages:
            lab[row][col] = lab[row-1][col] + lab[row][col - 1]


print(lab[R][C])
