import random

print("Hi welcome to the game, This is a number guessing game.\nYou got 7 chances to guess the number. Let's start "
      "the game")

number_to_guess = random.randrange(100)
chances = 7
guess_count = 0

while guess_count < chances:
    guess_count += 1
    my_guess = int(input("Please enter your guess - "))
    if my_guess == number_to_guess:
        print(f'The number is {number_to_guess} and you found it right !! in the {guess_count} attempt')
        break
    elif my_guess != number_to_guess and guess_count >= chances:
        print(f'Oops sorry, The number is {number_to_guess} better luck next time')
    elif my_guess > number_to_guess:
        print('Your guess is higher ')
    elif my_guess < number_to_guess:
        print('Your guess is lesser')
