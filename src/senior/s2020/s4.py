table = input()

# duplicate string for circular handling
dub = table * 2

n = len(table)
# psa - prefix sum array
# psaA[i]:the cumulative count of A from the start of dub up to index i - 1
psaA = [0] * (2 * n + 1)
psaB = [0] * (2 * n + 1)
psaC = [0] * (2 * n + 1)

# count occurrences for A, B, C until a given index
for index in range(1, 2*n+1):
    psaA[index] = psaA[index-1]
    psaB[index] = psaB[index-1]
    psaC[index] = psaC[index-1]
    if dub[index-1] == 'A':
        psaA[index] = psaA[index-1] + 1
    if dub[index-1] == 'B':
        psaB[index] = psaB[index-1] + 1
    if dub[index-1] == 'C':
        psaC[index] = psaC[index-1] + 1

# target group size for A, B, C
a = table.count('A')
b = table.count('B')
c = table.count('C')

ans = float('inf')

print(psaA)
print(psaB)
print(psaC)
# sliding window
for i in range(n):
    # calculate swaps to group A
    a_in_window = psaA[i + a] - psaA[i]
    a_swap = a - a_in_window

    # first approach, build group A then group B
    # calculate swaps to group B
    b_in_window = psaB[i + a + b] - psaB[i + a]
    b_swap = b - b_in_window

    # second approach, build group A then group C
    # calculate swaps to group C
    c_in_window = psaC[i + a + c] - psaC[i + a]
    c_swap = c - c_in_window

    # consider the overlap, e.g. swaps are counted twice
    b_in_a = psaB[i+a] - psaB[i]
    a_in_b = psaA[i+a+b] - psaA[i+a]
    c_in_a = psaC[i+a] - psaC[i]
    a_in_c = psaA[i+a+c] - psaA[i+a]

    # first approach, build group A then group B
    option1 = a_swap + b_swap - min(b_in_a, a_in_b)
    # second approach, build group A then group C
    option2 = a_swap + c_swap - min(c_in_a, a_in_c)

    ans = min(ans, option1, option2)

print(ans)