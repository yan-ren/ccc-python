# read the number of columns
num_columns = int(input())

# read the two rows of tile colors
row1 = list(input().split())
row2 = list(input().split())

# initialize variables
perimeter = 0

# loop through two list check how many ones
for i in row1:
    if i == "1":
        perimeter += 3

for i in row2:
    if i == "1":
        perimeter += 3

# loop again check adjacent triangle
index = 0
while index < len(row1) - 1:
    # check right side
    if row1[index] == "1" and row1[index+1] == "1":
        perimeter -= 2
    # check bottom
    if index % 2 == 0 and row1[index] == "1" and row2[index] == "1":
        perimeter -= 2
    index += 1

while index < len(row2) - 1:
    # check right side
    if row2[index] == "1" and row2[index+1] == "1":
        perimeter -= 2

print(perimeter)
'''
7
0 0 1 1 0 1 0
0 0 1 0 1 0 0
'''