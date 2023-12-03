
def isUnique(num):
    '''
    str(num) --> "12345"
    list(str(num)) --> ["1", "2", "3","4", "5"]
    '''
    l = list(str(num))
    return len(l) == len(set(l))



print(isUnique(12345))
