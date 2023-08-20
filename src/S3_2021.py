# get inputs and save all points into the list
N = int(input())
P = []
W = []
D = []

while N > 0:
    items = input().split(" ")
    P.append(int(items[0]))
    W.append(int(items[1]))
    D.append(int(items[2]))
    N -= 1

# apply binary search
left = 0
right = 1000000000

# given a point at position c, calculate what's the sum of time that all points P needs to move
def min_time(c):
    time = 0
    index = 0
    while index < len(P):
        dist = abs(c - P[index])
        if dist > D[index]:
            time += int((dist - D[index]) * W[index])
        index += 1
    return time


while left < right:
    c = (left + right + 1) / 2
    # compare c point to the left of c
    if min_time(c) <= min_time(c - 1):
        left = c # continue to find c on the right, meaning move left boundary to the c
    else:
        right = c - 1

print(min_time(left))

'''
graph algorithm
'''
a = 1
b = 1
print(a ^ b)