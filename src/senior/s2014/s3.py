test_cases = int(input())
test_inputs = []

# Collecting input for all test cases
for _ in range(test_cases):
    cars = []
    num_cars = int(input())
    for _ in range(num_cars):
        cars.append(int(input()))
    test_inputs.append(cars)

# Processing each test case
for car_list in test_inputs:
    branch = []
    current_car = 1

    while True:
        if car_list:
            if car_list[-1] == current_car:
                car_list.pop()
                current_car += 1
            elif branch and branch[-1] == current_car:
                branch.pop()
                current_car += 1
            else:
                branch.append(car_list.pop())
        elif branch:
            if branch[-1] == current_car:
                branch.pop()
                current_car += 1
            else:
                print('N')
                break
        else:
            print('Y')
            break
