favourite = int(input())
games = int(input())

# score for each team, 1, 2, 3, 4
score = [0, 0, 0, 0, 0]
remaining = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

for i in range(games):
    input_line = list(map(int, input().split(" "))) # [1, 3, 7, 5]
    match = [input_line[0], input_line[1]]

    if match in remaining:
        remaining.remove(match)
    if match[::-1] in remaining:
        remaining.remove(match)
    # update score
    if input_line[2] > input_line[3]:
        score[input_line[0]] += 3
    elif input_line[2] < input_line[3]:
        score[input_line[1]] += 3
    else:
        score[input_line[0]] += 1
        score[input_line[0]] += 1


def remaining_games(remaining, score, favourite):
    if len(remaining) == 0:
        if score[favourite] == max(score):
            for i in range(1, len(score)):
                if i != favourite and score[i] == score[favourite]:
                    return 0
            return 1
        return 0

    current_game = remaining[0]
    # [:] make a copy of the list to avoid original list being modified
    # first team in current game wins
    case1 = score[:]
    case1[current_game[0]] += 3
    # second team in current game wins
    case2 = score[:]
    case2[current_game[1]] += 3
    # tie
    case3 = score[:]
    case3[current_game[0]] += 1
    case3[current_game[1]] += 1

    return remaining_games(remaining[1:], case1, favourite) + remaining_games(remaining[1:], case2, favourite) + remaining_games(remaining[1:], case3, favourite)


print(remaining_games(remaining, score, favourite))
