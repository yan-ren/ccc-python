from collections import deque

def is_possible_to_escape(M, N, room):
    visited = [[False] * N for _ in range(M)]
    queue = deque([(0, 0)])

    while queue:
        r, c = queue.popleft()
        x = room[r][c]
        visited[r][c] = True

        if r == M - 1 and c == N - 1:
            return "yes"

        for i in range(1, int(x**0.5) + 1):
            if x % i == 0:
                a, b = i, x // i
                if 1 <= a <= M and 1 <= b <= N and not visited[a - 1][b - 1]:
                    queue.append((a - 1, b - 1))
                if 1 <= b <= M and 1 <= a <= N and not visited[b - 1][a - 1]:
                    queue.append((b - 1, a - 1))

    return "no"

# Read input
M = int(input())
N = int(input())
room = [list(map(int, input().split())) for _ in range(M)]

# Check if it's possible to escape
result = is_possible_to_escape(M, N, room)

# Output the result
print(result)

'''
https://dmoj.ca/problem/ccc20s2
Batch #1 (0/0 points)
Case #1:	AC	[0.030s,	10.63 MB]

Batch #2 (1/1 points)
Case #1:	AC	[0.030s,	10.57 MB]
Case #2:	AC	[0.030s,	10.67 MB]
Case #3:	AC	[0.030s,	10.52 MB]
Case #4:	AC	[0.030s,	10.58 MB]
Case #5:	AC	[0.030s,	10.51 MB]
Case #6:	AC	[0.030s,	10.63 MB]
Case #7:	AC	[0.031s,	10.52 MB]

Batch #3 (2/2 points)
Case #1:	AC	[0.030s,	10.52 MB]
Case #2:	AC	[0.030s,	10.53 MB]
Case #3:	AC	[0.030s,	10.58 MB]
Case #4:	AC	[0.030s,	10.70 MB]
Case #5:	AC	[0.030s,	10.52 MB]
Case #6:	AC	[0.030s,	10.68 MB]

Batch #4 (4/4 points)
Case #1:	AC	[0.030s,	10.54 MB]
Case #2:	AC	[0.030s,	10.75 MB]
Case #3:	AC	[0.030s,	10.52 MB]
Case #4:	AC	[0.030s,	10.52 MB]
Case #5:	AC	[0.030s,	10.68 MB]

Batch #5 (4/4 points)
Case #1:	AC	[0.031s,	10.57 MB]
Case #2:	AC	[0.031s,	10.71 MB]
Case #3:	AC	[0.030s,	10.66 MB]
Case #4:	AC	[0.031s,	10.57 MB]

Batch #6 (0/2 points)
Case #1:	AC	[0.036s,	12.37 MB]
Case #2:	AC	[0.049s,	11.82 MB]
Case #3:	TLE	[>2.000s,	13.47 MB]
Case #4:	—		
Case #5:	—		
Case #6:	—		

Batch #7 (0/2 points)
Case #1:	AC	[0.175s,	57.39 MB]
Case #2:	TLE	[>2.000s,	47.41 MB]
Case #3:	—		
Case #4:	—		
Case #5:	—		
Case #6:	—		
Case #7:	—		


Resources: ---, 57.39 MB
Final score: 11/15 (7.333/10 points)
'''