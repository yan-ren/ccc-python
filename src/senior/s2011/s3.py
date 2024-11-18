def is_in_crystal(m, x, y):
    # base case, when at level 1, check if coordinate is crystal
    if m == 1:
        return (x == 2 and y == 1) or (1 <= x <= 3 and y == 0)

    # check if the current coordinate, when scaled down to the previous level
    if is_in_crystal(m - 1, x // 5, y // 5):
        return True

    '''
    check if current coordinate is in the 'head' area, if it is, when scale down to previous
    level, this coordinate should be still within the crystal
    '''
    '''
    y // 5 is check if we are above level 1

    '''
    if (y // 5 > 0) and is_in_crystal(m - 1, x // 5, y // 5 - 1) \
            and is_in_crystal(1, x % 5, y % 5):
        return True


T = int(input())

for _ in range(T):
    m, x, y = map(int, input().split())
    if is_in_crystal(m, x, y):
        print('crystal')
    else:
        print('empty')