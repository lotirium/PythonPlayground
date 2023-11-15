import sys
import random


def run_guess(n, answer):
    if 0 < n < 11:
        if n == answer:
            print("Congrats! You won!")
            return True
        else:
            print("Try a different number: ")
            return False
    else:
        print("please return a number in range of 1-10")
        return False


# answer = random.randint(int(sys.argv[1]), int(sys.argv[2]))
if __name__ == "__main__":
    answer = random.randint(1, 10)
    while True:
        try:
            n = int(input(f"Enter a number between 1-10: "))
            if (run_guess(n, answer)):
                break
        except ValueError:
            print("Please enter a number")
            continue
