import random

def guess_number():
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your guess (1-100): "))
        attempts += 1

        if guess == target_number:
            print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
            break
        elif guess < target_number:
            print("Too low. Try again.")
        else:
            print(f"Too high. Try again.")

# Main program
print("Welcome to the Number Guessing Game!")
guess_number()
