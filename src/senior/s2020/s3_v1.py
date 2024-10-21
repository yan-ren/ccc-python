def count_distinct_permutations(N, H):
    '''
    Use built-in hash function to track duplicated substring, this give 7/15, due to
    recalculating hash value exceeds Time limit
    :param N: pattern
    :param H: text
    :return:
    '''

    if len(N) > len(H):
        return 0

    pattern_freq = [0] * 26
    text_freq = [0] * 26

    for i in range(len(N)):
        pattern_freq[ord(N[i]) - 97] += 1

    # build text_freq for first sliding window
    for i in range(len(N)):
        text_freq[ord(H[i]) - 97] += 1

    # track substring for duplicates
    seen = set()

    if pattern_freq == text_freq:
        seen.add(hash(H[:len(N)]))

    # sliding window over the text
    for i in range(len(N), len(H)):
        outgoing_char = H[i - len(N)]
        incoming_char = H[i]

        text_freq[ord(outgoing_char) - 97] -= 1
        text_freq[ord(incoming_char) - 97] += 1

        if text_freq == pattern_freq:
            seen.add(hash(H[i - len(N) + 1: i + 1]))

    return len(seen)


N = input()
H = input()

result = count_distinct_permutations(N, H)
print(result)

'''
side note

to build character frequency counter, there are a least three options
1. dictionary
2. Counter
3. list
'''
# from collections import Counter
#
# data = ['apple', 'banana', 'apple', 'orange', 'banana']
# count = Counter(data)
# print(count)
#
# text = 'hello hi world'
# count = Counter(text)
# print(count)