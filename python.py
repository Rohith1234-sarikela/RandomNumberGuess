import random

lower_bound = 1
upper_bound = 100
target_number = random.randint(lower_bound, upper_bound)
max_attempts = 10

print(f"Guess the number between {lower_bound} and {upper_bound}. You have {max_attempts} attempts.")

for attempt in range(1, max_attempts + 1):
    try:
        guess = int(input(f"Attempt {attempt}/{max_attempts}: Enter your guess: "))
        
        if guess < lower_bound or guess > upper_bound:
            print(f"Please enter a number between {lower_bound} and {upper_bound}.")
            continue

        if guess < target_number:
            print("Too low!")
        elif guess > target_number:
            print("Too high!")
        else:
            print(f"🎉 Congratulations! You guessed the number {target_number} in {attempt} attempts!")
            break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

else:
    print(f"😢 Sorry! You've used all {max_attempts} attempts. The correct number was {target_number}.")
