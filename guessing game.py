import random

correct = False
number = random.randint(1, 100)
guess_count = 0

while not correct:
    guess = input("please enter a number between 1-100:")
    guess_count +=1

    if int(guess) == number :
        print(f"Congrats! This took {guess_count} guesses")
        break
    elif int(guess) > number:
        print("your guess is to high")
    elif int(guess) < number:
        print("your guess is to low!")
    