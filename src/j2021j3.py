def convert_inputs():
    list_of_elements = []
    while True:
        input1 = input()
        if input1 != "99999":
            n_list = []
            n_list.append(int(input1[0]) + int(input1[1]))
            n_list.append(int(input1[2:]))
            list_of_elements.append(n_list)
            # 57234 00907
            # [[12, 234], [0, 907]]
        else:
            break
    return list_of_elements


def order_declaring():
    lists_of_elements = convert_inputs()
    direction = ""
    steps = 0
    for i in lists_of_elements:
        if i[0] % 2 == 0 and i[0] != 0:
            direction = "right"
            steps = i[1]
        elif i[0] == 0:
            steps = i[1]
        else:
            direction = "left"
            steps = i[1]
        print(direction, steps)


order_declaring()
