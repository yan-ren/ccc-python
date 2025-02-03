'''
what is a good triplet
All of three points are not on the same side

total triplets - bad triplets = good triplets

total triplets = (N * (N-1) * (N-2)) / 3!
math - discrete math, probability and random theory

find the bad triplets:
loop each point 'i' on circle, for each 'i' find the opposite point

case 1
- if one point exists at 'i' and take two other points in between the i and opposite
those two point have to be on the same side between the i and opposite
case 2
- if two points exist at 'i' and take one other point
case 3
- if three points exist at 'i', they still form a bad triplet

edge case:
If the circumference is even, will overall calculate the triplet

for example in the sample input, look at i = 0, and opposite = 5

when i = 0, we take p1, p3, p4 as bad triplet, but
later when i = 5, we also take p3, p4, p1 again
'''

N, C = map(int, input().split())

count = [0] * C # total number of points at each position on the circle
total_points = [0] * C # total amount of points from 0 to index

locations = map(int, input().split())
for location in locations:
    count[location] += 1

total_points[0] = count[0]
for i in range(1, C):
    total_points[i] = total_points[i-1] + count[i]

total_triplets = N * (N-1) * (N-2) // 6 # combination rules

for i in range(C):
    opposite = (i + C // 2) % C
    points_between = 0 # points between i and opposite, not including i

    if i + 1 <= opposite:
        # when i is on the upper half of the circle
        points_between = total_points[opposite] - total_points[i]
    else:
        # when i is on the lower half of the circle
        points_between = total_points[opposite] + (total_points[C - 1] - total_points[i])

    # case 1
    total_triplets -= count[i] * (points_between * (points_between - 1) // 2)
    # case 2
    total_triplets -= (count[i] * (count[i] - 1) // 2) * points_between
    # case 3
    total_triplets -= count[i] * (count[i] - 1) * (count[i] - 2) // 6

if C % 2 == 0:
    for i in range(C // 2):
        # add back
        opposite = i + C // 2
        # 2 points from i and 1 point from opposite
        total_triplets += (count[i] * (count[i] - 1) // 2) * count[opposite]
        # 1 point from i and 2 points from opposite
        total_triplets += count[i] * (count[opposite] * (count[opposite] - 1) // 2)

print(total_triplets)
