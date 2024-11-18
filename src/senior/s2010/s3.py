'''
Obervation: for firehose the possible length is between 0 to 1,000,000

key thing:
1. how to place the fire hydrant
- try each house as the starting point to place the fire hydrant

2. depends on how to place the fire hydrant,
how to find the max length of fire hose that is required to connect all houses
- because we know that the max length of firehose can only be a number from (0, 1000000),
we try each possible value using binary search O(logN)

- binary search step: first try 250,000, if too small, try (250,000 + 1000000) / 2
                     or if 250,000 works, need to look at lower range: (0+250,000) / 2

'''

circumference = 1_000_000 # circumference of the village
H = int(input()) # number of the houses
houses = [int(input()) for _ in range(H)]
houses.sort()
# helpful method here: duplicate houses list
# with offset to handle circular village
houses += [house + circumference for house in houses]

K = int(input()) # number of hydrant

# is all house covered tih k hydrants for a given hose
def can_cover_all_houses(hose_length, start_house_index):
    cover_range = hose_length * 2
    placed_hydrant = 1
    start = houses[start_house_index]
    hose_range = start + cover_range

    for house in houses[start_house_index: start_house_index + H]:
        if house > hose_range:
            # need to place another hydrant to cover the current house
            placed_hydrant += 1
            hose_range = house + cover_range # new fire hydrant is placed to cover the current house
            if placed_hydrant > K:
                return False

    return True

'''

'''
def binary_search_for_hose_length(start_house):
    left, right = 0, circumference
    best = circumference

    while left <= right:
        mid = (left + right) // 2
        if can_cover_all_houses(mid, start_house):
            # try a small number to see, if it can still cover all houses
            right = mid - 1
            best = min(best, mid)
        else:
            left = mid + 1

    return best


'''
Try each house as starting point (first house to cover for placing the first hydrant)
find the min hose length that can cover all houses, by using binary search to find the  min hose length
from (0, 1000000)
'''
result = circumference

for i in range(H):
    result = min(result, binary_search_for_hose_length(i))

print(result)
