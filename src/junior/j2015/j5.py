'''
n pieces of pie
k people

pie(n, k)

give one pie to one of the people, so only need to worry about the rest of people
pie(n-1, k-1)

leave one pie to all of people, then distrubute the remainiig to all people
pie(n-k, k)

n = 8
k = 2

pie(8, 2) = pie(7, 1) + pie(6, 2)
pie(6, 2) = pie(5, 1) + pie(4, 2)
pie(4, 2) = pie(3, 1) + pie(2, 2)


pie(n, k) = pie(n-1, k-1) + pie(n-k, k)

dynamic programming:
top down approach (memorization)
bottom up approach
'''

piemap = dict()
def pie(pieces, people):
    if pieces < people:
        return 0
    if people == 1 or pieces == people:
        return 1

    if (pieces, people) in piemap:
        return piemap[(pieces, people)]

    piemap[(pieces, people)] = pie(pieces - 1, people - 1) + pie(pieces - people, people)
    return piemap[(pieces, people)]


n = int(input())
k = int(input())

print(pie(n, k))