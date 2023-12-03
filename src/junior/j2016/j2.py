index = 0
source = []
while index < 4:
    line = input("")
    line_list = line.split(" ")
    # source.append(
    #     [int(line_list[0]), int(line_list[1]), int(line_list[2]), int(line_list[3])]
    # )

    source.append([int(i) for i in line_list])
    index += 1

print(source)
