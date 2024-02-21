'''
Given two list of numbers, two lists with same length

list1: [9, 3, 15, 2, 5]
list2: [19, 2, 14, 7, 1]

total minimum, match the number that as closely together as possible

list1: [2, 3, 5, 9, 15]
list2: [1, 2, 7, 14, 19]

total maximum, we want to keep the largest from each list.
Pair the maxi from one list the smallest value from other list

list1: [2, 3, 5, 9, 15]
list2: [19, 14, 7, 2, 1]
'''
problem_type = int(input())
length = int(input())
list_a = sorted(map(int, input().split()))
list_b = sorted(map(int, input().split()))


def getMax():
    total = 0

    for i in range(length):
        total += max(int(list_a[i]), int(list_b[length - 1 - i]))

    return total


def getMin():
    total = 0

    for i in range(length):
        total += max(int(list_a[i]), int(list_b[i]))

    return total


if problem_type == 1:
    print(getMin())
else:
    print(getMax())