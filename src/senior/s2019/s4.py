n, k = map(int, input().split())
enjoyment_values = [0] + list(map(int, input().split()))  # 1-indexed for easier translation

max_size = int(1e6 + 233)
fenwick_tree = [0] * max_size
dp = [0] * max_size
max_dp = [0] * max_size
visit_day = [0] * max_size
max_suffix_value = [0] * max_size  # max suffix enjoyment value of the previous day


def update(index, value):
    x = max_size - index - 1
    while x < max_size:
        fenwick_tree[x] = max(fenwick_tree[x], value)
        x += x & -x


def query_suffix_max(index):
    result = 0
    x = max_size - index - 1
    while x > 0:
        result = max(result, fenwick_tree[x])
        x -= x & -x
    return result


# Preprocessing days
day_counter = 1
for i in range(n % k, n + 1, k):
    visit_day[day_counter] = i
    day_counter += 1

current_day, backtrack, current_max = 1, 0, 0
for i in range(1, n + 1):
    limit = visit_day[current_day - 1]
    current_max = max(enjoyment_values[i], current_max)
    while max_suffix_value[backtrack] <= current_max and max(limit, i - k) <= backtrack:
        max_suffix_value[backtrack] = enjoyment_values[i]
        update(backtrack, max_dp[backtrack] + enjoyment_values[i])
        if max_suffix_value[backtrack - 1] <= current_max and max(limit, i - k) <= backtrack - 1:
            backtrack -= 1
        else:
            break
    if max(limit, i - k) > backtrack:
        update(backtrack + 1, max_dp[backtrack + 1] + current_max)
        backtrack += 1
        max_suffix_value[backtrack] = current_max

    dp[i] = query_suffix_max(max(limit, i - k))
    if i % k == 0:
        max_for_update = 0
        for j in range(i, max(visit_day[current_day], i - k) - 1, -1):
            update(j, dp[j] + max_for_update)
            max_for_update = max(max_for_update, enjoyment_values[j])
            max_dp[j] = max(max_dp[j + 1], dp[j])
        current_day += 1
        backtrack = i
        current_max = 0

print(dp[n])
