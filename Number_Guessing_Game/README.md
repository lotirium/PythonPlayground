# Number Guessing Game

## Overview
This is a simple yet engaging number guessing game written in Python. The game challenges players to guess a random number within a specified range and difficulty level. Players are given a certain number of guesses and are scored based on their performance.

## Features
- **Difficulty Levels**: Players can choose from three difficulty levels (Easy, Medium, Hard), which determines the range of the random number.
- **Score Tracking**: The game tracks the player's score, decreasing with each incorrect guess.
- **Replayability**: Players can choose to play again after each game without restarting the application.
- **Command Line Arguments**: Difficulty level can be set via command line arguments.

## How to Run
1. Ensure you have Python installed on your system.
2. Download or clone this repository to your local machine.
3. Open a terminal and navigate to the project directory.
4. Run the game using the command:

`python number_guessing_game.py [difficulty]`

Replace `[difficulty]` with `easy`, `medium`, or `hard`. If no difficulty is specified, the game defaults to 'easy'.

## How to Play
- After starting the game, you will be prompted to enter your guess for the random number.
- Based on your guess, the game will provide hints such as "Try a lower number" or "Try a higher number."
- Keep guessing until you find the correct number or run out of guesses.
- After the game ends, your score will be displayed, and you will be asked if you want to play again.

## Scoring System
- You start with a score of 100.
- Each incorrect guess deducts 20 points from your score.

## Future Enhancements
- Implementation of a GUI for a more user-friendly experience.
- Addition of a leaderboard to track high scores among players.
- Introduction of a time-based challenge mode.

## Feedback
Feel free to fork this project, submit issues, or send suggestions for future improvements. Your feedback is highly appreciated!
