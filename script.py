letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10
]

# Add lowercase letters and duplicate points
letters += [letter.lower() for letter in letters]
points *= 2

# Map letters to points
# Assign 0 points to space
letter_to_points = dict(zip(letters, points))
letter_to_points[" "] = 0 

# Function to calculate the score of a single word
def score_word(word):
    total = 0
    for letter in word:
        total += letter_to_points.get(letter, 0)
    return total

# Dictionary mapping players to words they've played
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

# Function to calculate total points per player
def update_point_totals():
    standings = {}
    for player, words in player_to_words.items():
        if not words:  # handle empty word list
            standings[player] = 0
            continue
        player_points = sum(score_word(word) for word in words)
        standings[player] = player_points
    return standings


# Function to allow a player to play a new word
def play_word(player, word):
    if player in player_to_words:
        normalized_word = word.upper()
        player_to_words[player].append(normalized_word)
    else:
        print(f"Player {player} does not exist.")

# Main execution
# Calculate initial standings and update standings 
def main():
    player_standings = update_point_totals()
    print("\nInitial player points:")
    print(player_standings)

    # Example: player1 plays "CODE"
    play_word("player1", "CODE")
    
    player_standings = update_point_totals()
    print("\nUpdated player points after new word:")
    print(player_standings)

    print("\nWords per player:")
    print(player_to_words)

    # Example: calculate score for a specific word
    brownie_score = score_word("BROWNIE")
    print("\nScore for 'BROWNIE':", brownie_score)

# Ensure main only runs if script is executed directly
if __name__ == "__main__":
    main()