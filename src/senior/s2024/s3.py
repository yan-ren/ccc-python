'''
given example:
6
0 1 2 3 4 5
0 0 2 2 5 5

B = [0 0 2 2 5 5]
has three block
[0 0] [2 2] [5 5]
each block match blocks with subarrays in A
[0 0] match to [0 1] in A, swipe right on [0 1]
[2 2] match to [2 3] in A, swipe right on [2 3]
[5 5] match to [4 5] in A, swipe left on [4 5]

General step to create B from A
1. segment B into block
2. matching block in A, check if there is swipe exists that can
transform matching block A into block B
'''
n = int(input())
array_A = list(map(int, input().split()))
array_B = list(map(int, input().split()))

# segment array B into blocks of continguous identical values
block_value = [array_B[0]]
block_range = []

block_start, block_end = 0, 0
current_value = array_B[0]

for i in range(1, n):
    if array_B[i] == current_value:
        block_end += 1
    else:
        block_range.append((block_start, block_end))
        block_start, block_end = i, i
        current_value = array_B[i]
        block_value.append(current_value)

# append the last block
block_range.append((block_start, block_end))

# print(block_value)
# print(block_range)

# match blocks in B into subarrays in A
current_block = 0
left_swipes = []
right_swipes = []
for i in range(n):
    if current_block == len(block_value):
        break # all block are matched
    if array_A[i] == block_value[current_block]:
        if block_range[current_block][0] < i:
            left_swipes.append((block_range[current_block][0], i))
        if block_range[current_block][1] > i:
            right_swipes.append((i, block_range[current_block][1]))

        current_block += 1 # move to the next block

if current_block == len(block_value):
    print("YES")
    print(len(left_swipes) + len(right_swipes))

    # print swipe operation
    for left in left_swipes:
        print("L", left[0], left[1])
    # print right swipe, in reverse order,
    '''
    This is necessary because a right swipe operation modifies the array elements to the right 
    of a specific index. If these operations are applied in the wrong order, 
    earlier operations can overwrite the effects of later ones, breaking the desired transformation.
    e.g.
    A = [0, 1, 2, 3]
    B = [0, 0, 0, 2]
    swipe right from 0 to 2 gives [0, 0, 0, 3] this makes 2 gone, breaks the following swipe
    when iterating in reverse order, we handle rightmost segments first.
    '''
    for right in reversed(right_swipes):
        print("R", right[0], right[1])
else:
    print("NO")


