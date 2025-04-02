import random
lower_bound = 1
upper_bound = 100
target_number = random.randint(lower_bound, upper_bound)

max_attempts = 10
for attempt in range(max_attempts):
    guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
    if guess < target_number:
        print("Too low!")
    elif guess > target_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number!")
        break