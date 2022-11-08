shelf = input()

# count size for section_L, section_M, section_S
def get_count(shelf):
    section_L = 0
    section_M = 0
    section_S = 0
    for i in shelf:
        if i == "L":
            section_L += 1
        elif i == "M":
            section_M += 1
        else:
            section_S += 1
    return [section_L, section_M, section_S]


section_L_size, section_M_size, section_S_size = get_count(shelf)
section_L = get_count(shelf[:section_L_size])
section_M = get_count(shelf[section_L_size : section_L_size + section_M_size])
section_S = get_count(shelf[section_L_size + section_M_size :])
# print(section_L)
# print(section_M)
# print(section_S)

# perform swap1
# the number of swap1 can be done between section L and M, depends on
# how many M in section L and how many L in section M
swap1_L_M = min(section_L[1], section_M[0])
swap1_M_S = min(section_M[2], section_S[1])
swap1_L_S = min(section_L[2], section_S[0])

swap1 = sum([swap1_L_M, swap1_M_S, swap1_L_S])

# update number of L, M, S in section L, M, S
section_L[0] = section_L[0] + swap1_L_M + swap1_L_S
section_L[1] = section_L[1] - swap1_L_M
section_L[2] = section_L[2] - swap1_L_S

section_M[0] = section_M[0] - swap1_L_M
section_M[1] = section_M[1] + swap1_L_M + swap1_M_S
section_S[2] = section_M[2] - swap1_L_S

section_S[0] = section_S[0] - swap1_L_S
section_S[1] = section_S[1] - swap1_M_S
section_S[2] = section_S[2] + swap1_L_S + swap1_M_S

# swap2
print(swap1 + (section_L[1] + section_L[2]) * 2)
