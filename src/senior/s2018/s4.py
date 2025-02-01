'''
mem = {}

def solve(weight):
    if weight in mem:
        return mem[weight]

    if weight <= 2:
        return 1

    total = 0
    prev_subtree = 1
    child_weight = weight // 2 # when k = 2, largest weight for subtree

    while child_weight > 0:
        subtrees = weight // child_weight
        # subtress - prev_subtree count only new configurations
        total += solve(child_weight) * (subtrees - prev_subtree)
        prev_subtree = subtrees
        child_weight = weight // (subtrees + 1)

    mem[weight] = total
    return total


n = int(input())
print(solve(n))
'''

'''optional topic

bitwise operator in python

& | ^ ~ << >>

a = 5 # binary 0101
b = 3 # binary 0011

result = a & b # binary 0001
print(result) # output 1
'''
x = 7
if x & 1:
    print('odd')
else:
    print('even')

x = 10
print(x << 1) # 10 * 2
print(x >> 1) # 10 // 2
