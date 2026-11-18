# QUESTION 1 - NUMBER GUESSING GAME

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

attempts = 3

while attempts > 0:
    guess = int(input("Guess the number (between 1 and 10): "))

    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess between 1 and 10.")
        continue

    attempts = attempts - 1

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break

    elif guess > secret_number:
        print("Too high. Try again.")

    else:
        print("Too low. Try again.")

else:
    print("Better luck next time!")

# QUESTION 2 - MULTIPLICATION TABLE

num = int(input("Enter the number for which you want the multiplication table: "))

for i in range(1, 11):
    result = num * i
    print(num, "x", i, "=", result)

# QUESTION 3 - BMI CALCULATOR

def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

result = calculate_bmi(weight, height)

print("Your BMI is:", round(result, 2))
