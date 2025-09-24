
import random

def guess_game():
    ans = random.randint(1, 100)
    min_val, max_val = 1, 100

    while True:
        try:
            guess = int(input(f"Guess the number in range: {min_val} ~ {max_val}\n> "))
            if guess == ans:
                print(f"Congratulations, you guessed it! The answer was {ans}")
                break
            elif guess < ans:
                min_val = guess + 1
            else:
                max_val = guess - 1
        except (ValueError, EOFError):
            print("\nInput ended.")
            break

if __name__ == "__main__":
    guess_game()
