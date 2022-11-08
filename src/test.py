import math


P = int(input())
N = int(input())
R = int(input())

total = N
day = 0

while total <= P:
    day += 1
    total += N * math.pow(R, day)
print(day)
