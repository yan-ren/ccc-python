speed_limit = int(input('Enter the speed limit: '))
car_speed = int(input('Enter the recorded speed of the car: '))

if car_speed <= speed_limit:
    print('Congratulations, you are within the speed limit')
elif  speed_limit + 1 <= car_speed <= speed_limit + 20:
    print('You are speeding and your fine is $ 100')
elif  speed_limit + 21 <= car_speed <= speed_limit + 30:
    print('You are speeding and your fine is $ 270')
elif  speed_limit + 31 <= car_speed:
    print('You are speeding and your fine is $ 500')