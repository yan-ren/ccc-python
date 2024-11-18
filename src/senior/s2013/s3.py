'''
Simulate all the remaining games with all possible outcomes

using DFS
'''
fav_team = int(input())
games_played = int(input())

# scores for the four teams
scores = {1: 0, 2: 0, 3: 0, 4: 0}

# keep track of the games already played
played_matches = set()

def simulate(remaining_matches, match_index, scores, fav_team):
    # if all remaining matches are simulated, check if the fav team has the most points
    if match_index == len(remaining_matches):
        max_score = max(scores.values())
        if scores[fav_team] == max_score and list(scores.values()).count(max_score) == 1:
            return 1 # fav_team is the only winner
        return 0

    team1, team2 = remaining_matches[match_index]

    total_wins = 0

    # case 1: team1 wins
    scores[team1] += 3
    total_wins += simulate(remaining_matches, match_index + 1, scores, fav_team)
    scores[team1] -= 3

    # case 2: team2 wins
    scores[team2] += 3
    total_wins += simulate(remaining_matches, match_index + 1, scores, fav_team)
    scores[team2] -= 3

    # case 3: tie
    scores[team1] += 1
    scores[team2] += 1
    total_wins += simulate(remaining_matches, match_index + 1, scores, fav_team)
    scores[team1] -= 1
    scores[team2] -= 1

    return total_wins


# get games that already played
for _ in range(games_played):
    t1, t2, s1, s2 = tuple(map(int, input().split())) # -> [1, 3, 7, 5]
    played_matches.add((t1, t2))

    if s1 > s2:
        scores[t1] += 3
    elif s2 > s1:
        scores[t2] += 3
    else: # tie
        scores[t1] += 1
        scores[t2] += 1


all_matches = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
remaining_matches = []

for match in all_matches:
    if match not in played_matches:
        remaining_matches.append(match)

print(simulate(remaining_matches, 0, scores, fav_team))
