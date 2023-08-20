l = []
numbers = []
while True:
    ask = input('')
    if ask == '99999':
        for h in range(len(l)):
            print(l[h], numbers[h])
        break
    sum1 = int(ask[0])+int(ask[1])
    if sum1 == 0:
        l.append(l[-1])
        numbers.append(ask[2:])
    else:
        g = sum1/2
        if g == int(g):
            l.append('right')
            numbers.append(ask[2:])
        elif g != int(g):
            l.append('left')
            numbers.append(ask[2:])


#
def secret_instructions():
    lis = []
    x = input()
    while x != "99999":
        lis.append(x)
        x = input()

    return lis


a = secret_instructions()
current = ""
for i in a:
    temp = i[:2]
    temp1 = i[2:]
    if ((int(temp[0]) + int(temp[1])) % 2 == 0) and (int(temp[0]) + int(temp[1])) != 0:
        current = "right"
    elif (int(temp[0]) + int(temp[1])) % 2 == 1:
        current = "left"

    print(current + " " + temp1)
