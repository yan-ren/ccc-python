from collections import deque
import sys

M = int(input())
N = int(input())

visited = [False for _ in range(M * N + 1)]
rooms = [[] for _ in range(M * N + 1)]

for row in range(1, M + 1):
    for col, val in enumerate(map(int, input().split()), start=1):
        if val <= M * N:
            rooms[row * col].append(val)

q = deque([1])

while q:
    cur = q.popleft()
    if cur == M * N:
        print('yes')
        sys.exit(0)

    for value in rooms[cur]:
        if not visited[value]:
            visited[value] = True
            q.append(value)

print("no")

'''
https://dmoj.ca/problem/ccc20s2
Batch #1 (0/0 points)
Case #1:	AC	[0.030s,	10.59 MB]

Batch #2 (1/1 points)
Case #1:	AC	[0.030s,	10.53 MB]
Case #2:	AC	[0.030s,	10.59 MB]
Case #3:	AC	[0.030s,	10.63 MB]
Case #4:	AC	[0.030s,	10.48 MB]
Case #5:	AC	[0.030s,	10.48 MB]
Case #6:	AC	[0.030s,	10.62 MB]
Case #7:	AC	[0.030s,	10.44 MB]

Batch #3 (2/2 points)
Case #1:	AC	[0.030s,	10.55 MB]
Case #2:	AC	[0.030s,	10.66 MB]
Case #3:	AC	[0.030s,	10.55 MB]
Case #4:	AC	[0.030s,	10.60 MB]
Case #5:	AC	[0.031s,	10.50 MB]
Case #6:	AC	[0.030s,	10.51 MB]

Batch #4 (4/4 points)
Case #1:	AC	[0.031s,	10.69 MB]
Case #2:	AC	[0.030s,	10.60 MB]
Case #3:	AC	[0.030s,	10.48 MB]
Case #4:	AC	[0.030s,	10.59 MB]
Case #5:	AC	[0.030s,	10.69 MB]

Batch #5 (4/4 points)
Case #1:	AC	[0.030s,	10.61 MB]
Case #2:	AC	[0.031s,	10.64 MB]
Case #3:	AC	[0.030s,	10.69 MB]
Case #4:	AC	[0.031s,	10.65 MB]

Batch #6 (2/2 points)
Case #1:	AC	[0.047s,	15.46 MB]
Case #2:	AC	[0.047s,	14.71 MB]
Case #3:	AC	[0.055s,	15.35 MB]
Case #4:	AC	[0.048s,	14.85 MB]
Case #5:	AC	[0.048s,	14.77 MB]
Case #6:	AC	[0.169s,	36.90 MB]

Batch #7 (2/2 points)
Case #1:	AC	[0.749s,	128.54 MB]
Case #2:	AC	[0.767s,	117.09 MB]
Case #3:	AC	[0.791s,	121.23 MB]
Case #4:	AC	[0.784s,	128.59 MB]
Case #5:	AC	[1.012s,	128.56 MB]
Case #6:	AC	[1.037s,	129.30 MB]
Case #7:	AC	[1.016s,	129.10 MB]


Resources: 7.269s, 129.30 MB
Maximum single-case runtime: 1.037s
Final score: 15/15 (10.0/10 points)
'''