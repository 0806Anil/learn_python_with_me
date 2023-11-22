import random

def roll_dice():
    return random.randint(1, 6)

# Main program
print("Welcome to the Dice Roller!")
input("Press Enter to roll the die...")

result = roll_dice()
print(f"You rolled a {result}.")
