'''
greedy algorithm: make local optimal decision at each step with the goal
of building a globally optimal solution

The greedy part for this problem: we fill the sequence by maximizing the number
of good samples at each step. Selecting the highest possible distinct pitch until
it becomes necessary to reuse pitches to meet the constraints

why greed algorithm works:
Greedy algorithm helps maximize the number of good samples initially by selecting
distinct pitches. when the number of good samples exceeds the required value (K),
start reusing pitches to reduce the number of good samples while still maintaining
a valid sequence.

key:

the sequence starts with distinct pitches and when the number of good samples become
too large, we begin to reuse previous pitches to lower the sample count
'''


def good_samples(n, m, k):
    ans = []

    for i in range(n):
        rem = n - i - 1  # remaining positions after the current one

        # the maximum pitch we can assign at this position
        cur = min(k - rem, m)
        '''
        k - rem: tell us how many good samples we can afford  to use for the current position while
        ensuring that there are still enough positions left to meet the required number of good samples

        if we assign pitches that contribute too many samples, we would run out of good samples to fill 
        the remaining positions
        '''

        if cur <= 0:
            break

        if cur > i:
            val = min(m, i + 1)  # we use the lowest available pitch
            cur = val
        else:
            val = ans[i - cur]  # reuse a previous pitch to reduce good samples

        ans.append(val)
        k -= cur  # decrease the required good samples

    if k == 0 and len(ans) == n:
        print(' '.join(map(str, ans)))
    else:
        print(-1)


n, m, k = map(int, input().split())
good_samples(n, m, k)