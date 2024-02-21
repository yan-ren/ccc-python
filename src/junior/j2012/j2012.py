def final_goal(coins):
    config = ''
    for i in range(1, coins+1):
        config += i + ' '

    return config.strip()

def valid_move(start, end):
    if start == ' ':
        return False
    elif end == ' ':
        return True
    else:
        # the last digit is the coin can be moved
        return int(start) % 10 < int(end) % 10

'''
This function makes new move string, for example we have '1|2|3' want to move index 1 value to index 2 value, 
we call function 
new_move_String(['1', '2', '3'], 1, 2)
function will return 
'1||32'
'''
def new_move_string(coins_position, start, end):
    move_coin = coins_position[start][len(coins_position[start]) - 1:]
    coins_position[start] = coins_position[start][0:len(coins_position[start]) - 1]
    coins_position[end] += str(move_coin)
    coins_position[end] = coins_position[end].strip()

    temp = ''
    for coin in coins_position:
        if coin == '':
            temp += ' |'
        else:
            temp += coin + '|'

    return temp


def make_move(order):
    next_move = set()
    coins_position = order.split('|')
    for i in range(len(coins_position) - 1):
        # can we move i to i+1?
        if valid_move(coins_position[i], coins_position[i+1]):
            next_move = next_move | new_move_string(coins_position, i, i+1)
        # can we move i+1 to i?
        elif valid_move(coins_position[i+1], coins_position[i]):
            next_move = next_move | new_move_string(coins_position, i+1, 1)

    return next_move

def bfs(current_level, seen, move):
    if final_goal(coins) in current_level:
        return move
    elif len(current_level) == 0:
        return -1

    next_level = set()
    seen = seen | current_level
    for s in current_level:
        next_level.add(make_move(s))

    # if any move in seen already, need to remove from next_level
    next_level = next_level - seen
    return bfs(next_level, seen, move + 1)


coins = int(input())

while coins != 0:
    order = set()
    s = set()
    # replace space with |, coins string look like 1|2|3
    order.add(input().replace(' ', '|'))
    count = bfs(order, s, 0)
    if count >= 0:
        print(count)
    else:
        print('IMPOSSIBLE')
    coins = int(input())