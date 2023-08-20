# read first group, create a dictionary that represetn paris should be in the same group
n = int(input())
same_group = {}
while n > 0:
    items = input().split(" ")
    if items[0] in same_group:
        same_group[items[0]].add(items[1])
    else:
        same_group[items[0]] = {items[1]}
    n -= 1

n = int(input())
diff_group = {}
while n > 0:
    items = input().split(" ")
    if items[0] in diff_group:
        diff_group[items[0]].add(items[1])
    else:
        diff_group[items[0]] = {items[1]}
    n -= 1

# check each pair
n = int(input())
violation = 0
while n > 0:
    a, b, c = items = input().split()
    # same group checking
    if a in same_group and b not in same_group[a] and c not in same_group[a]:
        violation += 1
    if b in same_group and a not in same_group[b] and c not in same_group[b]:
        violation += 1
    if c in same_group and a not in same_group[c] and b not in same_group[c]:
        violation += 1

    # diff group checking
    if a in diff_group and b in diff_group[a]:
        violation += 1
    if a in diff_group and c in diff_group[a]:
        violation += 1
    if b in diff_group and a in diff_group[b]:
        violation += 1
    if b in diff_group and c in diff_group[b]:
        violation += 1
    if c in diff_group and a in diff_group[c]:
        violation += 1
    if c in diff_group and b in diff_group[c]:
        violation += 1

    n -= 1

print(same_group)
print(diff_group)
print(violation)
