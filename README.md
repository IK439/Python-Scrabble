# Python-Scrabble

This Python script calculates Scrabble-style scores for players based on the words they have played. It supports both uppercase and lowercase letters and allows you to add new words for players while updating their total points.

## Features

- Calculate the score of individual words.
- Maintain a dictionary of players and the words they've played.
- Update total points for each player.
- Add new words for a player, with automatic score updating.
- Handles empty word lists and unknown letters gracefully.
- Normalizes all words to uppercase for consistent scoring.

## How it Works

1. **Letter Points Mapping**  
   Each letter (A-Z, case-insensitive) is mapped to its corresponding Scrabble points.

2. **Scoring Words**  
   The `score_word(word)` function calculates the total points for a given word.

3. **Player Scores**  
   The `player_to_words` dictionary stores each player's played words.  
   `update_point_totals()` calculates the total points for all players.

4. **Playing New Words**  
   The `play_word(player, word)` function allows a player to add a new word. The word is automatically normalized to uppercase.

5. **Main Execution**  
   Running the script directly will:
   - Display initial player points.
   - Add a sample word (`"CODE"`) for `player1`.
   - Display updated standings.
   - Show words per player.
   - Calculate the score for the word `"BROWNIE"` as an example.
