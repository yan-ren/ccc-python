import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())

r = [int(input()) for _ in range(n)]

readings = Counter(r)

readings.most_common()

best = [i for i in readings.keys() if readings[i] == max(readings.values())]

if len(best) > 1:
    print(max(best) - min(best))

else:
    second = [i for i in readings.keys() if readings[i] == sorted(list(set(readings.values())), reverse=True)[1]]

    if len(second) == 1:
        print(abs(best[0] - second[0]))

    else:
        s = 0

        for i in second:
            s = max(s, abs(best[0] - i))

        print(s)