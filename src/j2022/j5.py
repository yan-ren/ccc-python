'''
Idea

Search base on trees, we can create the largest square right or down until we hit a tree or a bondary
This forms a rectangle, the biggest square in this rectangle is the min(length of rectangle, width rectangle)
'''

# prepare the inputs
N = int(input())
number_of_trees = int(input())
trees = []
for i in range(number_of_trees):
    coordinate = input().split() # "4 7" -> ["4", "7"]
    trees.append((int(coordinate[0]), int(coordinate[1])))

# consider edge as tree
trees.append((0, 0))
trees.append([N+1, N+1])

# sort trees top down
trees = sorted(trees, key=lambda coord: coord[0])

# loop through each tree as a boundary, since tree is sorted from top down, all previous trees are ignored in loop
i = 0
biggest_square = 0
while i < len(trees):
    horizontal = [0, N+1]
    # for each tree that is lower than trees[i], they are the lower boundary
    j = i + 1
    while j < len(trees):
        width = 0
        height = trees[j][0] - trees[i][0] - 1
        horizontal.sort()
        # for each horizontal line, they form the rectangle
        k = 1
        while k < len(horizontal):
            # width = horizontal[k] - horizontal[k-1]
            width = max(width, horizontal[k] - horizontal[k-1] - 1)
            k += 1
        biggest_square = max(biggest_square, min(height, width))
        horizontal.append(trees[j][1]) # for each trees[j] their y coordinate is the horizontal boundry
        j += 1
    i += 1

print(biggest_square)