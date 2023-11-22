import sys
import random

def set_range(difficulty):
    if difficulty == 'easy':
        return 1, 10
    elif difficulty == 'medium':
        return 1, 50
    elif difficulty == 'hard':
        return 1, 100
    else:
        raise ValueError("Invalid difficulty level. You need to type 'easy', 'medium', or 'hard'")

def run_guess(num, answer, num_left):
    if num == answer:
        print("Congrats! You won!")
        return True
    else:
        if num_left > 1:
            hint = "Try a lower number" if num > answer else "Try a higher number"
            print(f"Wrong guess. {hint} You have {num_left - 1} guesses left")
        else:
            print(f"Sorry, you ran out of guesses, correct answer was {answer}")
        return False


def main(difficulty):


    if difficulty == 'easy':
        guesses_limit = 5
    elif difficulty == 'medium':
        guesses_limit = 25
    elif difficulty == 'hard':
        guesses_limit = 50

    start, end = set_range(difficulty)
    answer = random.randint(start, end)
    score = 100

    print(f"Guess a number between {start} and {end}. You have {guesses_limit} guesses")

    for _ in range(guesses_limit):
        valid_input = False

        while not valid_input:
            try:
                guess = int(input("Enter your number: "))
                valid_input = True
            except ValueError:
                print("Invalid input. Please enter a number")

        if run_guess(guess, answer, guesses_limit - _):
            break
        else:
            score -= 20
    print(f"Your score: {score}")
    return score


if __name__ == "__main__":
    playing = True
    best_score = 0

    while playing:
        try:
            difficulty = sys.argv[1].lower()
        except IndexError:
            difficulty = 'easy'

        score = main(difficulty)
        best_score = max(best_score, score)
        print(f"Best score: {best_score}")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            playing = False
