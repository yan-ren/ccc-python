N, M, R, C = map(int, input().split())

# when there is only one column but need non-palindromic rows
# or only one row but need non-palindromic columns
if (M == 1 and R < N) or (N == 1 and C < M):
    print("IMPOSSIBLE")
    exit(0)
# when all rows are palindromic, even number of columns
# but need an odd number of palindromic columns
elif R == N and M % 2 == 0 and C % 2 == 1:
    print("IMPOSSIBLE")
    exit(0)
# when all columns are palindromic, even number of rows
# but need an odd number of palindromic rows
elif C == M and N % 2 == 0 and R % 2 == 1:
    print("IMPOSSIBLE")
    exit(0)

# initialize the grid, but filling in the same letter, make all rows and columns are palindrome
grid = [['b' for _ in range(M)] for _ in range(N)]
# break all rows palindrome: set last character of each row to 'c'
for i in range(N):
    grid[i][M - 1] = 'c'
# break all columns
for j in range(M):
    grid[N-1][j] = 'd'

grid[N-1][M-1] = 'e'

# simplest case
if R == 0 and C != 0:
    for i in range(N):
        for j in range(C):
            if j == C - 1:
                grid[i][C - 1] = 'b'
            else:
                grid[i][j] = 'a'
elif C == 0 and R != 0:
    # skip the implementation
    pass
elif R == N and C < M:
    # all rows are palindrome, but need to reduce the number of palindromic columns
    # set all columns of the first N-1 rows to 'a', making them palindromic rows
    for i in range(N - 1):
        for j in range(M):
            grid[i][j] = 'a'

    c = C
    if C % 2 == 1:
        # if C is odd, set the middle column of the last row to 'a'
        grid[N-1][M//2] = 'a'
        c -= 1
    if c == 0:
        # if no more columns need to be set, adjust the bottom-right character
        grid[N-1][M-1] = 'd'
    else:
        # symmetrically set the columns of the last rows to 'a' to create the required number of
        # palindrome columns
        i, j = 0, M - 1
        while c > 0 and i <= j:
            grid[N-1][i] = 'a'
            grid[N-1][j] = 'a'
            i += 1
            j -= 1
            c -= 2
elif C == M and R < N:
    # all columns are palindrome, but need to reduce the number of palindrome rows
    # set the first M-1 columns of all rows to 'a', making them palindrome columns
    pass
else:
    for i in range(R):
        for j in range(M):
            grid[i][j] = 'a'

    for i in range(N):
        for j in range(C):
            grid[i][j] = 'a'

for row in grid:
    print(''.join(row))
