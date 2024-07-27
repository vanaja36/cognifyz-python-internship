import random
print("\t\t\t\t Number Guesser")
print("\t\t\t\t ............")

def feedback(guess, number, min_num,max_num):
    range_size = max_num - min_num
    if abs(guess - number) > range_size*0.2:
        if guess < number:
            print("Two low! Try again")
        else:
            print("Two high! Try again")
    else:
        print("Low! Try again" if guess < number else " High! Try again")

def guess_the_number(min_num, max_num):
    number = random.randint(min_num,max_num)
    while True:
        guess = int(input(f"Guess the number between {min_num} and {max_num} : "))
        if guess == number:
            print("Congratulations !! you guess the correct number ", number)
            break
        else:
            feedback(guess, number, min_num, max_num)
    play_again = input("Wanna play again?(y/n) :").lower()
    if play_again == 'y':
        guess_the_number(min_num, max_num)
    else:
        print("Thank you for playing!")
min_range = int(input("Enter the minimum number in the range : "))
max_range = int(input("Enter the maximum in the range : "))
guess_the_number(min_range, max_range)