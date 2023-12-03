m = int(input())
n = int(input())
k = int(input())

# 0 == Black, 1 == Gold
rows = [0] * m
columns = [0] * n

for i in range(k):
    choice = input().split()
    if choice[0] == 'R':
        rows[int(choice[1]) - 1] ^= 1
    else:
        columns[int(choice[1]) - 1] ^= 1

# combine and count
count = 0
for i in range(m):
    for j in range(n):
        count += rows[i] ^ columns[j]

print(count)
