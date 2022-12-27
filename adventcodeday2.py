# The following (until otherwise noted) is for both parts of Day 2)
with open('puzzle2.txt', 'r') as filename:
    lines = filename.readlines()

no_newline_list = []

for element in lines:
    removed_newlines = element.split('\n')
    if '' in removed_newlines:
        removed_newlines.remove('')
    no_newline_list.append(removed_newlines)

# print(no_newline_list)

no_spaces_list = []

for lst in no_newline_list:
    for element in lst:
        removed_spaces = element.split(' ')
        if '' in removed_spaces:
            removed_spaces.remove('')
        no_spaces_list.append(removed_spaces)

# print(no_spaces_list)

# The following (until otherwise noted) is of Day 2 Part 2
your_total = 0

for combo in no_spaces_list:
    if combo[0] == 'A':
        # Opponent chooses rock
        if combo[1] == 'X':
            # You lose (only 3 points added for choosing scissors)
            your_total += 3
        elif combo[1] == 'Y':
            # You draw with a rock (1 pt rock, 3 pts draw)
            your_total += 4
        elif combo[1] == 'Z':
            # You win with paper (2 pts paper, 6 pts win)
            your_total += 8
    elif combo[0] == 'B':
        # Opponent chooses paper
        if combo[1] == 'X':
            # You lose (only 1 pt added for choosing rock)
            your_total += 1
        elif combo[1] == 'Y':
            # You draw with paper (2 pt paper, 3 pt draw)
            your_total += 5
        elif combo[1] == 'Z':
            # You win with scissors (3 pt scissors, 6 pt win)
            your_total += 9
    elif combo[0] == 'C':
        # Opponent chooses scissors
        if combo[1] == 'X':
            # You lose (only 2 pt added for choosing paper)
            your_total += 2
        elif combo[1] == 'Y':
            # You draw with scissors (3 pt scissors, 3 pt draw)
            your_total += 6
        elif combo[1] == 'Z':
            # You win with rock (1 pt rock, 6 pt win)
            your_total += 7

print(your_total)



# For Day 2 Part 1
'''opponent_score = 0
your_score = 0
your_total = 0

score_per_game = []

for combo in no_spaces_list:
    for move_pos in range(len(combo)):
        if combo[move_pos] == 'A' or combo[move_pos] == 'X':
            # Rock
            if move_pos == 0:
                opponent_score += 1
                if combo[1] == 'X':
                    # Draw for rock
                    opponent_score += 3
                elif combo[1] == 'Z':
                    # Opponent beats your scissors
                    opponent_score += 6
                # Opponent loses to your paper does nothing
                # to opponent's score (all losses are like this)
            elif move_pos == 1:
                your_score += 1
                if combo[0] == 'A':
                    # Draw for rock
                    your_score += 3
                elif combo[0] == 'C':
                    # You beat opponent's scissors
                    your_score += 6
        elif combo[move_pos] == 'B' or combo[move_pos] == 'Y':
            # Paper
            if move_pos == 0:
                opponent_score += 2
                if combo[1] == 'Y':
                    # Draw for paper
                    opponent_score += 3
                elif combo[1] == 'X':
                    # Opponent beats your rock
                    opponent_score += 6
            elif move_pos == 1:
                your_score += 2
                if combo[0] == 'B':
                    # Draw for paper
                    your_score += 3
                elif combo[0] == 'A':
                    # You beat opponent's rock
                    your_score += 6
        elif combo[move_pos] == 'C' or combo[move_pos] == 'Z':
            # Scissors
            if move_pos == 0:
                opponent_score += 3
                if combo[1] == 'Z':
                    # Draw for scissors
                    opponent_score += 3
                elif combo[1] == 'Y':
                    # Opponent beats your paper
                    opponent_score += 6
            elif move_pos == 1:
                your_score += 3
                if combo[0] == 'C':
                    # Draw for scissors
                    your_score += 3
                elif combo[0] == 'B':
                    # You beat opponent's paper
                    your_score += 6
    both_scores = [opponent_score, your_score]
    score_per_game.append(both_scores)
    your_total += your_score
    opponent_score = 0
    your_score = 0

# print(score_per_game)
print(your_total)'''
