
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a playable Hangman game in Python using strings, loops, conditionals, user input, and random selection. Track guesses and show whether the player wins by revealing the word or loses by running out of attempts.

## 📝 Tasks

### 🛠️ Implement the guessing game

#### Description
Choose a secret word from a predefined list and let the player guess letters until the word is revealed or the allowed incorrect guesses are used.

#### Requirements
Completed program should:

- Randomly select one word from a predefined list.
- Accept a letter guess from the player on each turn.
- Display the correctly guessed letters in their positions and use underscores for letters not yet guessed.
- Track and display the number of incorrect guesses remaining.

### 🛠️ Handle game outcomes

#### Description
Update the game state after each guess and end the game when the player has either guessed the word or run out of allowed incorrect guesses.

#### Requirements
Completed program should:

- Reveal all matching positions when a guessed letter appears in the secret word.
- Reduce the remaining incorrect guesses for an incorrect guess.
- End when all letters in the secret word have been guessed or no incorrect guesses remain.
- Display a clear win or loss message and reveal the secret word if the player loses.
