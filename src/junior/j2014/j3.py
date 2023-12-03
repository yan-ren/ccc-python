rounds = int(input())

i = 0
sample =[]
while i < rounds:
    l = input().split(" ") # "5 6" -> ["5", "6"]
    sample.append((int(l[0]), int(l[1])))
    i+=1

# [(5,6), (6,6), (4,3), (5,2)]
# solution continue

antonia = 100
david = 100

for d in sample:
    if d[0] > d[1]:
        david -= d[0]
    elif d[1] > d[0]:
        antonia -= d[1]

print(antonia)
print(david)










# i = 0
# dices = []
# while i < rounds:
#     line = input() # '5 6'
#     items = line.split(" ") #['5', '6']
#     dices.append((int(items[0]), int(items[1])))


# dices -> [(5, 6), (6, 6), (4, 3), (5, 2)]



