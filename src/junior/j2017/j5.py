'''
length of each wood 1 <= L <= 2000
each board is made by two pieces of wood
length of each board 1 <= L <= 4000

N (the number of wood) is large

we need to find how many board with same length and then for different length
of board, how many times the board number is the same

use the list index to represent the length of wood, the value on each index represents number of wood
e.g. if a board height is 5, it can only be made from two wood length less than 5
'''
wood = [0] * 2001
board = [0] * 4001

### board[500] = 4
# skip the first value
input()
inputs = input().split(' ')
for i in inputs:
    wood[int(i)] += 1


i = 0
while i < len(wood):
    j = i
    while j < len(wood):
        # build the board with same length of the wood
        if j == i:
            board[i + j] += wood[i] // 2
        # build the board with the different length of the wood
        else:
            board[i + j] += min(wood[i], wood[j])
        j += 1
    i += 1

fence_length = 0
combines = 0

i = 0
while i < len(board):
    if board[i] > fence_length:
        fence_length = board[i]
        combines = 1
    elif board[i] == fence_length:
        combines += 1
    i += 1

print(fence_length, combines)
