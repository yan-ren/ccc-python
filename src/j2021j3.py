def convert_inputs():
    list_of_elements = []
    # x = True  not necessary to use variable
    while True:
        input1 = input()  # input() returns str, no need to convert str
        if input1 != "99999":
            n_list = []
            n_list.append(int(input1[0]) + int(input1[1]))
            n_list.append(int(input1[2:]))
            list_of_elements.append(n_list)
            # continue  redundent
        elif input1 == "99999":
            # x = False
            break
    # don't need 9999 in list
    # list_of_elements.append(99999)
    return list_of_elements


def order_declaring():
    direction = ""
    lists_of_elements = convert_inputs()
    direction = ""
    steps = 0
    for i in lists_of_elements:
        if i[0] % 2 == 0 and i[0] != 0:
            direction = "right"
            steps = i[1]
            print(direction, steps)
            # break    why use break?
        elif i[0] == 0:
            steps = i[1]
            print(direction, steps)
            # if direction == "":
            #     return "input error"
            # else:
            #     print(direction, i[1])
            #     # break
        else:
            direction = "left"
            steps = i[1]
            print(direction, steps)


order_declaring()
