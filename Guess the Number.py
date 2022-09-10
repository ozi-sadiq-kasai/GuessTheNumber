import random

computer_guess = random.randrange(1, 10)

user_number = int(input("Enter a number between 1 to 10: "))

while user_number != computer_guess:
    if user_number < computer_guess:
        print('Guess Higher, try again')
        user_number = (int(input("Enter a number: ")))
    else:
        print('Guess Lower, try again')
        user_number = (int(input("Enter a number: ")))
print('you got it')
