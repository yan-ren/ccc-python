# gather the input
total_time = int(input())
chores_number = int(input())

i = 0
chores = []
while i < chores_number:
    chores.append(int(input()))
    i += 1

# solution
chores.sort()
acc_time = 0
chores_count = 0
while acc_time + chores[chores_count] <= total_time:
    acc_time += chores[chores_count]
    chores_count += 1

print(chores_count)
