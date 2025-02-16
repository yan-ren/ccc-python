'''
Dynamic Programming - bottom up

we define dp[l][r] as the largest riceball size that can be formed from
index l to index r

dp[1][1]
if merging is not possible in given range, dp[l][r] = 0

introduce j and k, the middle part inside l and r
initially, j = l + 1, k = r

merging condition
if dp[l][j-1] == dp[k][r] and dp[j][k-1] is also valid riceball
we can merge entire range from l to r, which is dp[l][r]
dp[l][r] = dp[l][j-1] +dp[j][k-1] + dp[k][r]

if current j, k cannot cause merging, adjust the j, k base on sum of left section
and sum of right section

if left section < right section:
    j += 1
else:
    k -= 1
'''

n = int(input())

dp = [[0] * 402 for _ in range(402)]
ans = 0

arr = list(map(int, input().split()))

# fill dp with initial value, when l == r
for i in range(n):
    dp[i][i] = arr[i]
    ans = max(dp[i][i], ans)

# dp checks length from 1 to n
for length in range(1, n):
    for left in range(0, n - length):
        right = left + length
        j = left + 1
        k = right

        while j <= k:
            # sum of left section == sum of right section, and middle part is either a single ball
            # or a valid combination ball
            if dp[left][j-1] and dp[left][j - 1] == dp[k][right] and (j == k or dp[j][k-1]):
                dp[left][right] = dp[left][j - 1] + dp[j][k-1] + dp[k][right]
                ans = max(ans, dp[left][right])
                break
            # cannot merge with current j and k, need to adjust
            if dp[left][j - 1] < dp[k][right]:
                j += 1
            else:
                k -= 1

print(ans)
